from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    wait = WebDriverWait(driver, 5)
    links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

    assert len(links) == 9

    for link in links:
        assert link.is_displayed()

    assert "1" in links[0].text

    driver.quit()
