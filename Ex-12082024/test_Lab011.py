#Mini Project 1:
#open url
#find button
#click on it
#find inputbox for username and password
#enter username and password
#verify that on clicking submit button, user is logged in


from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_miniproject1():
    driver=webdriver.Chrome()
    driver.maximize_window()  #to maximize the window
#open url:
    driver.get("https://katalon-demo-cura.herokuapp.com/")

#find element(button):
    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")

#click on it:
    make_appointment_element.click()

#verify that url changes:
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.quit()  #to close all tabs
