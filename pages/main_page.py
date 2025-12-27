from pages.base_page import BasePage
from urls import LOGIN_URL, MAIN_PAGE_URL

class MainPage(BasePage):
    def open_login(self):
        """Открыть страницу авторизации."""
        self.open_url(LOGIN_URL)

    def open_main(self):
        """Открыть главную страницу."""
        self.open_url(MAIN_PAGE_URL)

    def get_ingredient_count(self, locator):
        """Получить текущее значение счётчика ингредиента."""
        return self.get_element_text(locator)