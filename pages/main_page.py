from pages.base_page import BasePage
from urls import LOGIN_URL, MAIN_PAGE_URL
from selenium.webdriver.support import expected_conditions as EC

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
    
    def wait_for_url(self, url):
        """Ожидать, пока URL не станет равным заданному."""
        self.wait.until(EC.url_to_be(url))

    def wait_for_element_to_be_displayed(self, locator):
        """Ожидать, пока элемент по локатору не станет видимым."""
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility_of_element(self, locator):
        """Ожидать, пока элемент по локатору не станет невидимым."""
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_text_to_be_present_in_element(self, locator, text):
        """Ожидать, пока текст появится в элементе по локатору."""
        self.wait.until(EC.text_to_be_present_in_element(locator, text))