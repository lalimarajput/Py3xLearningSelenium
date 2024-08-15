#Options class-customize behaviour of the browser during testing

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options


def test_open_vwologin():  #create an instance of chrome options
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920*1080")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    time.sleep(10)
