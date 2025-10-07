from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    QUESTION = (By.CSS_SELECTOR, ".accordion__button")
    ANSWER = (By.CSS_SELECTOR, ".accordion__panel")