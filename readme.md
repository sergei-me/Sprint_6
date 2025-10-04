# Автотесты для сервиса аренды самокатов

## Описание
Проект автоматизации тестирования веб-приложения по аренде самокатов с использованием Selenium, Pytest и Allure.  

Проверяются:

- Оформление заказа через верхнюю и нижнюю кнопки "Заказать".
- Переход по логотипам (Яндекс, Самокат).
- FAQ на главной странице и корректность отображения ответов.

## Технологии
- Python 3.x  
- Selenium WebDriver  
- Pytest  
- Allure для отчетов  

## Структура проекта
Sprint_6/
│
├─ pages/           # Page Object модели страниц
├─ tests/           # Тесты
├─ testdata/        # Тестовые данные (FAQ)
├─ config.py        # Настройки и константы (URL и др.)
├── conftest.py     # Фикстура драйвера
├─ requirements.txt # Зависимости
└─ README.md        # Документация

---

## Как запустить тесты

1. Установить зависимости:
```bash
pip install -r requirements.txt
```
2. Запуск всех тестов:
```
pytest tests/ --browser firefox

```
3. Запуск с формированием Allure отчета:
```
pytest tests/ --alluredir=allure-results
```
4. Сгенерировать HTML-отчет:
```
allure generate allure-results -o allure-report --clean
```
5. Открыть HTML-отчет в браузере:
```
allure open allure-report
```
