from selenium.webdriver.common.by import By


class CheckoutPage:
    """Класс для страницы оформления заказа"""

    def __init__(self, driver):
        """
        Инициализация страницы оформления

        :param driver: экземпляр веб-драйвера
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """
        Заполняет форму оформления заказа

        :param first_name: имя
        :param last_name: фамилия
        :param postal_code: почтовый индекс
        """
        element = self.driver.find_element(*self.first_name_input)
        element.send_keys(first_name)
        element = self.driver.find_element(*self.last_name_input)
        element.send_keys(last_name)
        element = self.driver.find_element(*self.postal_code_input)
        element.send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """
        Возвращает итоговую стоимость заказа

        :return: текст с итоговой стоимостью
        """
        return self.driver.find_element(*self.total_label).text
