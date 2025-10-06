from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Loc

class MainPageQuestions(BasePage):

    def accept_cookies(self):
        self.click(Loc.COOKIE_BUTTON)

    def open_question(self, index):
        questions = self.find_all(Loc.QUESTION)
        question = questions[index]
        
        self.scroll_to_center(question)
        self.js_click(question)

    def get_answer_text(self, index):
        answers = self.find_all(Loc.ANSWER)
        answer = answers[index]
        self.wait.until(EC.visibility_of(answer))
        return answer.text
