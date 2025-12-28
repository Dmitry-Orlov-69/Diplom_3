import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_feed_page import OrderFeedPage
from locators import BUTTON_CONSTRUCTOR, INGREDIENT_BUN_R2_D3, ORDER_MODAL, ORDER_ID_IN_MODAL, BUTTON_ORDER_FEED, ORDER_COLLECTION_FIELD, BUTTON_MAKE_ORDER
from urls import MAIN_PAGE_URL, ORDER_FEED_PAGE_URL

class TestOrderFeed:
    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_navigate_to_order_feed(browser):
        with allure.step("Открыть главную страницу"):
            order_feed_page = OrderFeedPage(browser)
            order_feed_page.open_main()

        with allure.step("Нажать на кнопку 'Лента заказов'"):
            order_feed_page.click(BUTTON_ORDER_FEED)

        with allure.step("Проверить, что произошёл переход на адрес ленты заказов"):
            order_feed_page.wait_for_url(ORDER_FEED_PAGE_URL)
            assert order_feed_page.browser.current_url == ORDER_FEED_PAGE_URL, "Переход на страницу 'Лента заказов' не состоялся"

    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_all_time_counter_increases(browser, unique_user, login_existing_user):
        with allure.step("Открыть страницу ленты заказов"):
            order_feed_page = OrderFeedPage(browser)
            order_feed_page.open_order_feed()

        with allure.step("Запоминаем текущее количество заказов в счётчике «Выполнено за всё время»"):
            initial_count = order_feed_page.get_counter_all_time()

        with allure.step("Нажать на кнопку 'Конструктор'"):
            order_feed_page.click(BUTTON_CONSTRUCTOR)

        with allure.step("Перетаскиваем ингредиент 'Флюоресцентная булка R2-D3' в поле сбора заказа"):
            order_feed_page.drag_and_drop(INGREDIENT_BUN_R2_D3, ORDER_COLLECTION_FIELD)

        with allure.step("Нажать на кнопку 'Оформить заказ'"):
            order_feed_page.click(BUTTON_MAKE_ORDER)

        with allure.step("Ожидаем появления идентификатора заказа"):
            order_feed_page.wait_for_element_to_be_displayed(ORDER_ID_IN_MODAL)

        with allure.step("Закрываем окно заказа и ожидаем его закрытия"):
            order_feed_page.close_modal()
            order_feed_page.wait_for_invisibility_of_element(ORDER_MODAL)

        with allure.step("Переход обратно на страницу 'Лента заказов'"):
            order_feed_page.click(BUTTON_ORDER_FEED)
            order_feed_page.wait_for_url(ORDER_FEED_PAGE_URL)

        with allure.step("Проверяем что в счётчике «Выполнено за всё время» увеличилось количество заказов"):
            updated_count = order_feed_page.get_counter_all_time()
            assert updated_count > initial_count, "Счётчик 'Выполнено за всё время' не увеличился"

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_counter_increases(browser, unique_user, login_existing_user):
        with allure.step("Открыть страницу ленты заказов"):
            order_feed_page = OrderFeedPage(browser)
            order_feed_page.open_order_feed()

        with allure.step("Запоминаем текущее количество заказов в счётчике «Выполнено за сегодня»"):
            initial_count = order_feed_page.get_counter_today()

        with allure.step("Нажать на кнопку 'Конструктор'"):
            order_feed_page.click(BUTTON_CONSTRUCTOR)

        with allure.step("Перетаскиваем ингредиент 'Флюоресцентная булка R2-D3' в поле сбора заказа"):
            order_feed_page.drag_and_drop(INGREDIENT_BUN_R2_D3, ORDER_COLLECTION_FIELD)

        with allure.step("Нажать на кнопку 'Оформить заказ'"):
            order_feed_page.click(BUTTON_MAKE_ORDER)

        with allure.step("Ожидаем появления идентификатора заказа"):
            order_feed_page.wait_for_element_to_be_displayed(ORDER_ID_IN_MODAL)

        with allure.step("Закрываем окно заказа и ожидаем его закрытия"):
            order_feed_page.close_modal()
            order_feed_page.wait_for_invisibility_of_element(ORDER_MODAL)

        with allure.step("Переход обратно на страницу 'Лента заказов'"):
            order_feed_page.click(BUTTON_ORDER_FEED)
            order_feed_page.wait_for_url(ORDER_FEED_PAGE_URL)

        with allure.step("Проверяем что в счётчике «Выполнено за сегодня» увеличилось количество заказов"):
            updated_count = order_feed_page.get_counter_today()
            assert updated_count > initial_count, "Счётчик 'Выполнено за сегодня' не увеличился"

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_appears_in_progress(browser, unique_user, login_existing_user):
        with allure.step("Открыть главную страницу"):
            order_feed_page = OrderFeedPage(browser)
            order_feed_page.open_main()

        with allure.step("Перетаскиваем ингредиент 'Флюоресцентная булка R2-D3' в поле сбора заказа"):
            order_feed_page.drag_and_drop(INGREDIENT_BUN_R2_D3, ORDER_COLLECTION_FIELD)

        with allure.step("Нажать на кнопку 'Оформить заказ'"):
            order_feed_page.click(BUTTON_MAKE_ORDER)

        with allure.step("Ожидаем появления идентификатора заказа"):
            order_feed_page.wait_for_element_to_be_displayed(ORDER_ID_IN_MODAL)
            order_id = order_feed_page.browser.find_element(*ORDER_ID_IN_MODAL).text

        with allure.step("Закрываем окно заказа и ожидаем его закрытия"):
            order_feed_page.close_modal()
            order_feed_page.wait_for_invisibility_of_element(ORDER_MODAL)

        with allure.step("Переход обратно на страницу 'Лента заказов'"):
            order_feed_page.click(BUTTON_ORDER_FEED)
            order_feed_page.wait_for_url(ORDER_FEED_PAGE_URL)

        with allure.step("Проверяем что номер идентификатора заказа появился в работе"):
            expected_order_id = f"0{order_id}"
            assert order_feed_page.is_order_in_progress(expected_order_id), f"Заказ с номером {expected_order_id} не найден в разделе 'В работе'"