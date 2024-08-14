import time

from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com/"
    time.sleep(10)
