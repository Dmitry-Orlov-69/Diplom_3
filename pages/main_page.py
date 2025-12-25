from urls import LOGIN_URL, MAIN_PAGE_URL
from selenium.webdriver.common.action_chains import ActionChains

class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def open_login(self):
        """Открыть страницу авторизации."""
        self.browser.get(LOGIN_URL)

    def open_main(self):
        """Открыть главную страницу."""
        self.browser.get(MAIN_PAGE_URL)

    def click(self, locator):
        """Нажать на элемент по локатору."""
        element = self.browser.find_element(*locator)
        element.click()

    def get_ingredient_count(self, locator):
        """Получить текущее значение счётчика ингредиента."""
        return self.browser.find_element(*locator).text

    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивать элемент с исходного местоположения в целевое."""
        source_element = self.browser.find_element(*source_locator)
        target_element = self.browser.find_element(*target_locator)
        action = ActionChains(self.browser)
        action.drag_and_drop(source_element, target_element).perform()