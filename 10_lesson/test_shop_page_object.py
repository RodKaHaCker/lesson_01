import allure
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка оформления заказа")
@allure.description(
    "Тест проверяет авторизацию, добавление товаров "
    "и итоговую стоимость заказа"
)
def test_shop_page_object():
    with allure.step("Открыть браузер и страницу магазина"):
        driver = webdriver.Firefox()
        login = LoginPage(driver)
        login.open("https://www.saucedemo.com/")

    with allure.step("Авторизоваться как standard_user"):
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавить три товара в корзину"):
        inventory = InventoryPage(driver)
        inventory.add_to_cart("sauce-labs-backpack")
        inventory.add_to_cart("sauce-labs-bolt-t-shirt")
        inventory.add_to_cart("sauce-labs-onesie")
        inventory.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart = CartPage(driver)
        cart.checkout()

    with allure.step("Заполнить форму заказа"):
        checkout = CheckoutPage(driver)
        checkout.fill_form("Иван", "Петров", "123456")

    with allure.step("Проверить итоговую стоимость"):
        total = checkout.get_total()
        assert "$58.29" in total, "Итоговая сумма не совпадает"

    with allure.step("Закрыть браузер"):
        driver.quit()
