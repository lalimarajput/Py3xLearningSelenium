#Incognito mode- to use chrome in incognito mode:

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    time.sleep(10)
