import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка работы калькулятора с задержкой")
@allure.description(
    "Тест проверяет, что калькулятор корректно вычисляет 7 + 8 = 15 "
    "с задержкой 45 секунд"
)
def test_calc_page_object():
    with allure.step("Открыть браузер и страницу калькулятора"):
        driver = webdriver.Chrome()
        calc = CalculatorPage(driver)
        calc.open(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    with allure.step("Установить задержку 45 секунд"):
        calc.set_delay("45")

    with allure.step("Ввести 7 + 8 ="):
        calc.click_button("7")
        calc.click_button("+")
        calc.click_button("8")
        calc.click_button("=")

    with allure.step("Проверить результат"):
        result = calc.get_result()
        assert result is True, "Результат не равен 15"

    with allure.step("Закрыть браузер"):
        driver.quit()
