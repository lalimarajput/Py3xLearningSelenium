import time

from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title=="Login - VWO"  #title in the address bar
    time.sleep(10)
