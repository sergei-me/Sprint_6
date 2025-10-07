from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Loc

class OrderPage(BasePage):

    def accept_cookies(self):
        self.click(Loc.COOKIE_BUTTON)
    
    def open_top_order_form(self):
        self.click(Loc.TOP_ORDER_BUTTON)
        self.wait_for_element(Loc.ORDER_HEADER_FIRST_PAGE)

    def open_bottom_order_form(self):
        bottom_button = self.find(Loc.BOTTOM_ORDER_BUTTON)
        self.scroll_to_center(bottom_button)
        bottom_button.click()
        self.wait_for_element(Loc.ORDER_HEADER_FIRST_PAGE)
        
    def fill_first_form(self, name, surname, address, phone, metro="Черкизовская"):
        self.enter_text(Loc.NAME_FIELD, name)
        self.enter_text(Loc.SURNAME_FIELD, surname)
        self.enter_text(Loc.ADRESS_FIELD, address)
        
        metro_input = self.find(Loc.METRO_FIELD)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro[:3])
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)
        
        self.enter_text(Loc.TELEPHONE_FIELD, phone)
        self.click(Loc.NEXT_PAGE_BUTTON)
        
        self.wait_for_element(Loc.ORDER_HEADER_SECOND_PAGE)

    def fill_second_form_with_comment(self, date, rental_period, color, comment=""):
        self.wait_for_element(Loc.ORDER_HEADER_SECOND_PAGE)
        
        date_field = self.find(Loc.ORDER_DATE_FIELD)
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        self.select_rental_period(rental_period)
        self.select_color(color)
        
        self.enter_text(Loc.COMMENT_FIELD, comment)
    
    def select_rental_period(self, period_text: str):
        field = self.find(Loc.RENTAL_PERIOD_FIELD)
        self.scroll_to_center(field)
        field.click()
        
        options = self.wait.until(EC.presence_of_all_elements_located(Loc.RENTAL_PERIOD_OPTION))
        if options:
            options[0].click()
        else:
            raise Exception("Не найдено ни одного варианта периода аренды")

    
    def select_color(self, color: str):
        locator = (By.XPATH, f"//input[@id='{color}']")
        self.click(locator)
    
    def confirm_order(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(Loc.OVERLAY))
        except TimeoutException:
            pass
        self.wait.until(EC.element_to_be_clickable(Loc.ORDER_BUTTON)).click()

        self.wait.until(EC.element_to_be_clickable(Loc.CONFIRM_YES_BUTTON)).click()

        self.wait.until(EC.visibility_of_element_located(Loc.ORDER_MODAL_HEADER))
   
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        
    def click_yandex_logo(self):
       self.click(Loc.YANDEX_LOGO_BUTTON)
    
    def click_scooter_logo(self):
       self.click(Loc.SCOOTER_LOGO_BUTTON)
       
    def click_yandex_logo_and_switch_tab(self):
        self.click(Loc.YANDEX_LOGO_BUTTON)
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(lambda d: d.current_url != "about:blank")
        return self.driver.current_url

    def is_current_url_contains(self, text):
        return text in self.driver.current_url
    
