from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop_page_object():
    driver = webdriver.Firefox()

    # Авторизация
    login = LoginPage(driver)
    login.open("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")

    # Добавление товаров
    inventory = InventoryPage(driver)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bolt-t-shirt")
    inventory.add_to_cart("sauce-labs-onesie")
    inventory.go_to_cart()

    # Оформление
    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Иван", "Петров", "123456")

    # Проверка итоговой суммы
    total = checkout.get_total()
    assert "$58.29" in total

    driver.quit()
