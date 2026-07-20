from selenium.webdriver.common.by import By


class LoginPage:
    """Класс для страницы авторизации магазина"""

    def __init__(self, driver):
        """
        Инициализация страницы авторизации

        :param driver: экземпляр веб-драйвера
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self, url: str) -> None:
        """
        Открывает страницу по указанному URL

        :param url: адрес страницы
        """
        self.driver.get(url)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию с указанными данными

        :param username: имя пользователя
        :param password: пароль
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
