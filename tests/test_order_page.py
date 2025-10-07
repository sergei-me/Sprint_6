import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse, parse_qs
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators as Loc

@allure.title("Заказ самоката через верхнюю кнопку")
@pytest.mark.parametrize("first_name, last_name, address, phone, date, duration, color, comment", [
    ("Иван", "Петров", "Москва, Кремль 1", "+79999999999", "03.10.2025", "сутки", "black", "Позвоните заранее"),
    ("Мария", "Сидорова", "Санкт-Петербург, Невский проспект 10", "+78888888888", "07.10.2025", "двое суток", "grey", "Доставить к 10 утра")
])
def test_order_scooter_top_button(driver, first_name, last_name, address, phone, date, duration, color, comment):
    order_page = OrderPage(driver)
    order_page.open_url()
    order_page.accept_cookies()

    with allure.step("Открытие формы заказа через верхнюю кнопку"):
        order_page.open_top_order_form()

    with allure.step("Заполнение формы"):
        order_page.fill_first_form(first_name, last_name, address, phone)
        order_page.fill_second_form_with_comment(date, duration, color, comment)

    with allure.step("Подтверждение заказа"):
        order_page.confirm_order()

    with allure.step("Проверка, что окно сформированного заказа отображается"):
        assert order_page.is_element_present(Loc.ORDER_MODAL_HEADER)


@allure.title("Заказ самоката через нижнюю кнопку")
@pytest.mark.parametrize("first_name, last_name, address, phone, date, duration, color, comment", [
    ("Иван", "Петров", "Москва, Кремль 1", "+79999999999", "04.10.2025", "трое суток", "grey", "Позвоните заранее"),
    ("Мария", "Сидорова", "Санкт-Петербург, Невский проспект 10", "+78888888888", "08.10.2025", "сутки", "black", "Без звонка")
])
def test_order_scooter_bottom_button(driver, first_name, last_name, address, phone, date, duration, color, comment):
    order_page = OrderPage(driver)
    order_page.open_url()
    order_page.accept_cookies()

    with allure.step("Открытие формы заказа через нижнюю кнопку"):
        order_page.open_bottom_order_form()

    with allure.step("Заполнение формы"):
        order_page.fill_first_form(first_name, last_name, address, phone)
        order_page.fill_second_form_with_comment(date, duration, color, comment)

    with allure.step("Подтверждение заказа"):
        order_page.confirm_order()

    with allure.step("Проверка, что окно сформированного заказа отображается"):
        assert order_page.is_element_present(Loc.ORDER_MODAL_HEADER)

@allure.title("Навигация по логотипу Яндекс")
@allure.description("Проверка, что клик по логотипу Яндекс ведёт на dzen.ru через retpath")
def test_click_yandex_logo(driver):
    order_page = OrderPage(driver)
    order_page.open_url()
    order_page.accept_cookies()

    with allure.step("Клик по логотипу Яндекс и переключение на новую вкладку"):
        new_tab_url = order_page.click_yandex_logo_and_switch_tab()

    with allure.step("Проверка перехода на Dzen"):
        assert "dzen.ru" in new_tab_url, f"Ожидался переход на Dzen, но получен URL: {new_tab_url}"


@allure.title("Навигация по логотипу Самокат")
@allure.description("Проверка перехода по клику на логотип Самоката")
def test_click_scooter_logo(driver):
    order_page = OrderPage(driver)
    order_page.open_url()
    order_page.accept_cookies()

    with allure.step("Клик по логотипу Самоката"):
        order_page.click_scooter_logo()

    with allure.step("Проверка открытия нужной страницы"):
        assert order_page.is_current_url_contains("qa-scooter.praktikum-services.ru")

