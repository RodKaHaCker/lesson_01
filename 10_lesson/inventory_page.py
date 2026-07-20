from selenium.webdriver.common.by import By


class InventoryPage:
    """Класс для главной страницы магазина"""

    def __init__(self, driver):
        """
        Инициализация главной страницы

        :param driver: экземпляр веб-драйвера
        """
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_id: str) -> None:
        """
        Добавляет товар в корзину по его ID

        :param product_id: идентификатор товара
        """
        self.driver.find_element(By.ID, f"add-to-cart-{product_id}").click()

    def go_to_cart(self) -> None:
        """Переходит в корзину"""
        self.driver.find_element(*self.cart_link).click()
