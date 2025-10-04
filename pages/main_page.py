from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class MainPageQuestions(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    QUESTION = (By.CSS_SELECTOR, ".accordion__button")
    ANSWER = (By.CSS_SELECTOR, ".accordion__panel")

    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)

    def open_question(self, index):
        questions = self.find_all(self.QUESTION)
        question = questions[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        self.driver.execute_script("arguments[0].click();", question)

    def get_answer_text(self, index):
        answers = self.find_all(self.ANSWER)
        answer = answers[index]
        WebDriverWait(self.driver, 10).until(EC.visibility_of(answer))
        return answer.text
