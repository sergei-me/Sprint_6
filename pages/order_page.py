from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class OrderPage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    TOP_ORDER_BUTTON = (By.CSS_SELECTOR, ".Button_Button__ra12g")
    BOTTOM_ORDER_BUTTON = (By.CSS_SELECTOR, ".Home_FinishButton__1_cWm button")
    
    ORDER_HEADER_FIRST_PAGE = (By.XPATH, "//div[contains(@class,'Order_Header__BZXOb') and text()='Для кого самокат']")
    
    NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CSS_SELECTOR, ".select-search__input")
    METRO_DROPDOWN_OPTION = (By.CSS_SELECTOR, ".select-search__select")
    TELEPHONE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "button.Button_Middle__1CSJM:nth-child(1)")
    
    ORDER_HEADER_SECOND_PAGE = (By.XPATH, "//div[contains(@class,'Order_Header__BZXOb') and text()='Про аренду']")
    
    ORDER_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    
    RENTAL_PERIOD_FIELD = (By.CSS_SELECTOR, ".Dropdown-placeholder")
    RENTAL_PERIOD_MENU = (By.CSS_SELECTOR, ".Dropdown-menu")
    RENTAL_PERIOD_OPTION = (By.CSS_SELECTOR, ".Dropdown-option")

    SCOOTER_COLOR_FIELD = (By.CSS_SELECTOR, ".Order_Checkboxes__3lWSI")
    COMMENT_FIELD = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Content__bmtHS')]//button[text()='Заказать']")
    OVERLAY = (By.CLASS_NAME, "Order_Overlay__3KW-T")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_MODAL_HEADER = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")
    
    SCOOTER_LOGO_BUTTON = (By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR > img:nth-child(1)")
    YANDEX_LOGO_BUTTON = (By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI > img:nth-child(1)")
    


    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)
    
    def open_order_form(self, position='top'):
        if position == "top":
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.TOP_ORDER_BUTTON)).click()
        elif position == "bottom":
            bottom_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BOTTOM_ORDER_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", bottom_button)
            bottom_button.click()
        else:
            raise ValueError("position must be 'top' or 'bottom'")
        self.wait_for_element(self.ORDER_HEADER_FIRST_PAGE)
        
    def fill_first_form(self, name, surname, address, phone, metro="Черкизовская"):
        self.enter_text(self.NAME_FIELD, name)
        self.enter_text(self.SURNAME_FIELD, surname)
        self.enter_text(self.ADRESS_FIELD, address)
        
        metro_input = self.find(self.METRO_FIELD)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro[:3])
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)
        
        self.enter_text(self.TELEPHONE_FIELD, phone)
        self.click(self.NEXT_PAGE_BUTTON)
        
        self.wait_for_element(self.ORDER_HEADER_SECOND_PAGE)

    def fill_second_form(self, date, rental_period, color, comment=""):
        self.wait_for_element(self.ORDER_HEADER_SECOND_PAGE)
        
        date_field = self.find(self.ORDER_DATE_FIELD)
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        self.select_rental_period(rental_period)
        self.select_color(color)
        
        if comment:
            self.enter_text(self.COMMENT_FIELD, comment)
    
    def select_rental_period(self, period_text: str):
        field = self.find(self.RENTAL_PERIOD_FIELD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
        field.click()
        options_locator = (By.CSS_SELECTOR, "body .Dropdown-option")
        options = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(options_locator))
        for option in options:
            if option.text.strip() == period_text:
                option.click()
                return
        raise Exception(f"Не найдена опция аренды: {period_text}")

    
    def select_color(self, color: str):
        locator = (By.XPATH, f"//input[@id='{color}']")
        self.click(locator)
    
    def confirm_order(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.OVERLAY))
        except TimeoutException:
            pass
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()

        yes_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CONFIRM_YES_BUTTON))
        yes_button.click()

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.ORDER_MODAL_HEADER))
   
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        
    def click_yandex_logo(self):
       self.click(self.YANDEX_LOGO_BUTTON)
    
    def click_scooter_logo(self):
       self.click(self.SCOOTER_LOGO_BUTTON)
