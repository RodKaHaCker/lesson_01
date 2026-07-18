from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    cookies_user1 = [
        {"name": "sessionid", "value": "3:1784143021.5.0.1770749588532:VlPPsg:a6a5.1.2:1|537391035.-1.2.3:1770749588.6:2196256036.7:1770749588|3:12044258.942477.9P2KO1_bktW7u2JIL6Zekf6qshM"}  # noqa
    ]

    cookies_user2 = [
        {"name": "sessionid", "value": "3:1784143021.5.0.1770749588532:VlPPsg:a6a5.1.2:1|537391035.-1.2.3:1770749588.6:2196256036.7:1770749588|3:12044258.942477.fakesign0000000000000000000"}  # noqa
    ]

    driver.get("https://gitflic.ru/")

    for cookie in cookies_user1:
        driver.add_cookie(cookie)

    driver.refresh()

    driver.get("https://gitflic.ru/user/rodkahacker")
    WebDriverWait(driver, 5).until(EC.url_contains("/user/"))
    url_user1 = driver.current_url

    driver.delete_all_cookies()

    for cookie in cookies_user2:
        driver.add_cookie(cookie)

    driver.refresh()

    driver.get("https://gitflic.ru/user/rodionsemenovyh")
    WebDriverWait(driver, 5).until(EC.url_contains("/user/"))
    url_user2 = driver.current_url

    assert url_user1 != url_user2

    driver.quit()
