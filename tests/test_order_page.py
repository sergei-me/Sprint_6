import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse
from pages.order_page import OrderPage

@allure.title("Заказ самоката в аренду")
@allure.description("Оформление заказа через верхнюю и нижнюю кнопки 'Заказать'")
@pytest.mark.parametrize("position", ["top", "bottom"])
def test_order_scooter_success(driver, position):
    order_page = OrderPage(driver)
    order_page.open()
    order_page.accept_cookies()
    with allure.step("Открытие формы заказа"):
        order_page.open_order_form(position)
    with allure.step("Заполнение первой части формы заказа"):
        order_page.fill_first_form("Иван", "Петров", "Москва, Кремль 1", "+79999999999")
    with allure.step("Заполнение второй части формы заказа"):
        order_page.fill_second_form("03.10.2025", "сутки", "black", "Позвоните заранее")
    with allure.step("Подтверждение заказа"):
        order_page.confirm_order()
    with allure.step("Проверка, что окно сформированного заказа отображается"):
        assert order_page.is_element_present(order_page.ORDER_MODAL_HEADER)

@allure.title("Навигация по логотипам")
@allure.description("Проверка перехода по клику на логотип")
@pytest.mark.parametrize("logo, expected_domain", [("yandex", "dzen.ru"), ("scooter", "qa-scooter.praktikum-services.ru")])
def test_click_logos(driver, logo, expected_domain):
    order_page = OrderPage(driver)
    order_page.open()
    order_page.accept_cookies()

    with allure.step(f"Клик по логотипу {logo}"):
        if logo == "yandex":
            order_page.click_yandex_logo()

            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            driver.switch_to.window(driver.window_handles[-1])
            WebDriverWait(driver, 10).until(lambda d: d.current_url != "about:blank")
        else:
            order_page.click_scooter_logo()

    with allure.step("Проверка открытия нужной страницы"):
        assert expected_domain in urlparse(driver.current_url).netloc

    if logo == "yandex":
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
