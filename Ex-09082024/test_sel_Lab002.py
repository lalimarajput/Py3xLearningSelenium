import time

from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com/"
    print (driver.session_id)
    time.sleep(10)
