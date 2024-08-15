#Page load strategy:

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    chrome_options = Options()
    chrome_options.add_argument("--page-load-strategy=normal")
    #we can use 'normal' or 'none' or 'eager'
    #none= no wait for resources to load
    #normal= wait for resources to load
    #eager=DOM access is ready but other resources are still loading
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
