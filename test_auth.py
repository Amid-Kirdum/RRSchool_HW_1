# "** Authorization**
# 1. Authorization using correct data (standard_user, secret_sauce)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
def test_auth_valid():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    driver.quit()
# 2. Authorization using incorrect data (user, user)
def test_auth_invalid():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('standard_user')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    driver.quit()