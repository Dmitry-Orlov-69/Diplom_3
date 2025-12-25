import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BUTTON_CONSTRUCTOR, CLOSED_INGREDIENT_DETAILS_MODAL_BUTTON, COUNTER_BUN_R2_D3, INGREDIENT_BUN_R2_D3, MODAL_INGREDIENT_DETAILS, ORDER_COLLECTION_FIELD, TEXT_INGREDIENT_DETAILS
from pages.main_page import MainPage
from urls import LOGIN_URL, MAIN_PAGE_URL

class Constructor:
    @allure.title("Переход по клику на «Конструктор»")
    def test_constructor_click(browser):
        with allure.step("Открыть страницу авторизации"):
            main_page = MainPage(browser)
            main_page.open_login()
            # Проверка перехода на страницу авторизации
            WebDriverWait(browser, 10).until(EC.url_to_be(LOGIN_URL))

        with allure.step("Нажать на кнопку «Конструктор»"):
            main_page.click(BUTTON_CONSTRUCTOR)

        with allure.step("Проверить переход на главную страницу с конструктором"):
            assert browser.current_url == MAIN_PAGE_URL, "Переход в Конструктор не произошёл"

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_ingredient_details(browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open_main()

        with allure.step("Нажать на ингредиент 'Флюоресцентная булка R2-D3'"):
            main_page.click(INGREDIENT_BUN_R2_D3)

        with allure.step("Проверить, что открылось окно с деталями ингредиента"):
            WebDriverWait(browser, 10).until(EC.presence_of_element_located(MODAL_INGREDIENT_DETAILS))
            assert browser.find_element(*MODAL_INGREDIENT_DETAILS).is_displayed(), "Окно с деталями ингредиента не видно"

        with allure.step("Проверить наличие надписи 'Детали ингредиента' в окне"):
            assert browser.find_element(*TEXT_INGREDIENT_DETAILS).is_displayed(), "Надпись 'Детали ингредиента' не видна"

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_details(browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open_main()

        with allure.step("Нажать на ингредиент 'Флюоресцентная булка R2-D3'"):
            main_page.click(INGREDIENT_BUN_R2_D3)

        with allure.step("Проверить, что открылось окно с деталями ингредиента"):
            WebDriverWait(browser, 10).until(EC.presence_of_element_located(MODAL_INGREDIENT_DETAILS))
            assert browser.find_element(*MODAL_INGREDIENT_DETAILS).is_displayed(), "Окно с деталями ингредиента не видно"

        with allure.step("Нажать на крестик, закрывающий окно с деталями ингредиента"):
            main_page.click(CLOSED_INGREDIENT_DETAILS_MODAL_BUTTON)

        with allure.step("Проверить исчезновение тёмного заднего фона и окна с деталями ингредиента"):
            WebDriverWait(browser, 10).until(EC.invisibility_of_element_located(MODAL_INGREDIENT_DETAILS))
            assert not browser.find_element(*MODAL_INGREDIENT_DETAILS).is_displayed(), "Окно с деталями ингредиента не исчезло"

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_ingredient_counter_increase(browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open_main()

        with allure.step("Проверить, что счётчик ингредиента 'Флюоресцентная булка R2-D3' равен нулю"):
            assert main_page.get_ingredient_count(COUNTER_BUN_R2_D3) == "0", "Счётчик ингредиента не равен нулю"

        with allure.step("Перетащить ингредиент 'Флюоресцентная булка R2-D3' из конструктора в поле сбора заказа"):
            # Используем локатор ORDER_COLLECTION_FIELD для указания поля сбора заказа
            main_page.drag_and_drop(INGREDIENT_BUN_R2_D3, ORDER_COLLECTION_FIELD)

        with allure.step("Проверить, что счётчик ингредиента 'Флюоресцентная булка R2-D3' равен 2"):
            WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(COUNTER_BUN_R2_D3, "2"))
            assert main_page.get_ingredient_count(COUNTER_BUN_R2_D3) == "2", "Счётчик ингредиента не увеличился до 2"