from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")

    # Найти ссылку по атрибуту href
    link = driver.find_element(By.XPATH, "//a[@href='/forms/post']")
    link.click()

    assert "/forms/post" in driver.current_url

    driver.back()

    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
