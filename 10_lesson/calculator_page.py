from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, seconds):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(seconds)

    def click_button(self, text):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self):
        wait = WebDriverWait(self.driver, 50)
        result_element = wait.until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        return result_element
