from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open_url(self, url):
        """Открыть URL."""
        self.browser.get(url)

    def click(self, locator):
        """Нажать на элемент по локатору."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_element_text(self, locator):
        """Получить текст элемента по локатору."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивать элемент с исходного местоположения в целевое."""
        source_element = self.browser.find_element(*source_locator)
        target_element = self.browser.find_element(*target_locator)
        ActionChains(self.browser).drag_and_drop(source_element, target_element).perform()

    def scroll_to_element(self, locator):
        """Прокрутить до элемента."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        return self.browser.current_url