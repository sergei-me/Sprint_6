import pytest
import allure
from pages.main_page import MainPageQuestions
from testdata.faq_data import FAQ_DATA
from config import BASE_URL

@allure.title("FAQ на главной")
@allure.description("Проверка текста отображения ответа на вопрос")
@pytest.mark.parametrize("index, expected", FAQ_DATA)
def test_check_faq_questions(driver, index, expected):
    page = MainPageQuestions(driver, BASE_URL)
    page.open()
    page.accept_cookies()
    with allure.step(f"Открытие вопроса {index}"):
        page.open_question(index)
    with allure.step(f"Проверка текста ответа"):
        text = page.get_answer_text(index)
        assert text == expected
