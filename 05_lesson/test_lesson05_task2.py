from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Родька")

    submit_button = driver.find_element(
        By.XPATH,
        "//button[text()='Submit order']"
    )
    submit_button.click()

    assert "/post" in driver.current_url

    driver.quit()
