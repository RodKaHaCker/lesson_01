from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    wait = WebDriverWait(driver, 10)
    hello_text = wait.until(EC.presence_of_element_located((By.ID, "finish"))).text

    driver.save_screenshot("dynamic_loading_screenshot.png")

    assert hello_text == "Hello World!"

    driver.quit()


if __name__ == "__main__":
    test_dynamic_loading()
