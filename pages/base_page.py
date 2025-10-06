from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def open_url(self, url=BASE_URL):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
    
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_center(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


