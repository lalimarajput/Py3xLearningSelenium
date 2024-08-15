#Remote Webdriver:

from selenium import webdriver
import time


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.page_source)  #to print the source code
    driver.close()  #to close the current tab
    time.sleep(10)
