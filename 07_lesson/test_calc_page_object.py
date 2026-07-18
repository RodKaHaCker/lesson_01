from selenium import webdriver
from calculator_page import CalculatorPage


def test_calc_page_object():
    driver = webdriver.Chrome()
    calc = CalculatorPage(driver)

    calc.open(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    calc.set_delay("45")

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    result = calc.get_result()
    assert result is True

    driver.quit()
