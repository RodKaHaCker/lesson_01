from selenium.webdriver.common.by import By


class CartPage:
    """Класс для страницы корзины"""

    def __init__(self, driver):
        """
        Инициализация страницы корзины

        :param driver: экземпляр веб-драйвера
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def checkout(self) -> None:
        """Нажимает кнопку оформления заказа"""
        self.driver.find_element(*self.checkout_button).click()
