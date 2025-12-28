from locators import CLOSED_ORDER_MODAL_BUTTON, COUNTER_ALL_TIME, COUNTER_TODAY, ORDER_IN_PROGRESS
from pages.base_page import BasePage
from urls import MAIN_PAGE_URL, ORDER_FEED_PAGE_URL
from selenium.webdriver.support import expected_conditions as EC

class OrderFeedPage(BasePage):
    def open_order_feed(self):
        """Открыть страницу ленты заказов."""
        self.open_url(ORDER_FEED_PAGE_URL)

    def open_main(self):
        """Открыть главную страницу."""
        self.open_url(MAIN_PAGE_URL)

    def get_counter_all_time(self):
        """Получить текущее значение счётчика 'Выполнено за всё время'."""
        return self.get_element_text(COUNTER_ALL_TIME)

    def close_modal(self):
        """Закрыть окно заказа."""
        self.click(CLOSED_ORDER_MODAL_BUTTON)

    def get_counter_today(self):
        """Получить текущее значение счётчика 'Выполнено за сегодня'."""
        return self.get_element_text(COUNTER_TODAY)

    def is_order_in_progress(self, order_id):
        """Проверить, что заказ с указанным номером находится в разделе 'В работе'."""
        return any(order_id in order.text for order in self.browser.find_elements(*ORDER_IN_PROGRESS))
    
    def wait_for_url(self, url):
        """Ожидать, пока URL не станет равным заданному."""
        self.wait.until(EC.url_to_be(url))

    def wait_for_element_to_be_displayed(self, locator):
        """Ожидать, пока элемент по локатору не станет видимым."""
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility_of_element(self, locator):
        """Ожидать, пока элемент по локатору не станет невидимым."""
        self.wait.until(EC.invisibility_of_element_located(locator))