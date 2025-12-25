from locators import CLOSED_ORDER_MODAL_BUTTON, COUNTER_ALL_TIME, COUNTER_TODAY, ORDER_IN_PROGRESS
from urls import MAIN_PAGE_URL, ORDER_FEED_PAGE_URL
from selenium.webdriver.common.action_chains import ActionChains

class OrderFeedPage:
    def __init__(self, browser):
        self.browser = browser

    def open_main(self):
        """Открыть главную страницу."""
        self.browser.get(MAIN_PAGE_URL)

    def click(self, locator):
        """Нажать на элемент, определённый локатором."""
        self.browser.find_element(*locator).click()

    def open_order_feed(self):
        """Открыть страницу ленты заказов."""
        self.browser.get(ORDER_FEED_PAGE_URL)

    def get_counter_all_time(self):
        """Получить текущее значение счётчика 'Выполнено за всё время'."""
        return self.browser.find_element(*COUNTER_ALL_TIME).text

    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивать элемент с исходного местоположения в целевое."""
        source_element = self.browser.find_element(*source_locator)
        target_element = self.browser.find_element(*target_locator)
        action = ActionChains(self.browser)
        action.drag_and_drop(source_element, target_element).perform()

    def close_modal(self):
        """Закрыть окно заказа."""
        self.browser.find_element(*CLOSED_ORDER_MODAL_BUTTON).click()

    def get_counter_today(self):
        """Получить текущее значение счётчика 'Выполнено за сегодня'."""
        return self.browser.find_element(*COUNTER_TODAY).text
    
    def is_order_in_progress(self, order_id):
        """Проверить, что заказ с указанным номером находится в разделе 'В работе'."""
        return any(order_id in order.text for order in self.browser.find_elements(*ORDER_IN_PROGRESS))