from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, postal_code):
        element = self.driver.find_element(*self.first_name_input)
        element.send_keys(first_name)
        element = self.driver.find_element(*self.last_name_input)
        element.send_keys(last_name)
        element = self.driver.find_element(*self.postal_code_input)
        element.send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        element = self.driver.find_element(*self.total_label)
        return element.text
