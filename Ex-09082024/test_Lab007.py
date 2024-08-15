#Adding Extension to chrome: download crx- Adblock Plus extension

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    chrome_options = Options()
    chrome_options.add_extension("C:/Users/lalim/Downloads/Adblock-Plus-free-ad-blocker-Chrome-Web-Store.crx")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://youtube.com")
    time.sleep(10)
