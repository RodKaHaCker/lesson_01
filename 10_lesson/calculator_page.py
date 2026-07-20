from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей калькулятора"""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора

        :param driver: экземпляр веб-драйвера
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self, url: str) -> None:
        """
        Открывает страницу по указанному URL

        :param url: адрес страницы
        """
        self.driver.get(url)

    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку в поле ввода

        :param seconds: значение задержки в секундах
        """
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(seconds)

    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку калькулятора с указанным текстом

        :param text: текст на кнопке
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self) -> bool:
        """
        Ожидает появления результата '15' и возвращает его наличие

        :return: True, если результат равен '15'
        """
        wait = WebDriverWait(self.driver, 50)
        return wait.until(EC.text_to_be_present_in_element(self.result_screen, "15"))
