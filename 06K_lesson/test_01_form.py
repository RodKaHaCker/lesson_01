from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажать Submit
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Проверка: Zip code подсвечен красным
    zip_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_field.get_attribute("class")

    # Проверка: остальные поля подсвечены зелёным
    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    for field_name in fields:
        field = driver.find_element(By.ID, field_name)
        assert "alert-success" in field.get_attribute("class")

    driver.quit()
