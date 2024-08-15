#Access Proxy server:

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    chrome_options = Options()
    proxy_server="https://your-proxy-server-ip:your-proxy-port"
    chrome_options.add_argument('--proxy-server='+ proxy_server)
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    time.sleep(10)
