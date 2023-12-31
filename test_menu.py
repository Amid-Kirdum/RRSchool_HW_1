# **Burger menu**
# 1. Logout
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#Passed
def test_auth_valid():
    driver.get("https://www.saucedemo.com/")

    url_before = driver.current_url

    username_field = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH,'//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(1)

    logout = driver.find_element(By.CSS_SELECTOR,'#logout_sidebar_link')
    logout.click()

    url_after = driver.current_url

    assert (url_after == url_before)

# 2. Checking the functionality of the "About" button in the menu

# FAILED
def test_button_about():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    time.sleep(2)

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()

    time.sleep(2)

    button_about = driver.find_element(By.XPATH,'//a[@id="inventory_sidebar_link"]')
    button_about.click()

    time.sleep(2)

    assert driver.current_url == "https://saucelabs.com/"

    driver.quit()

# 3. Проверка работоспособности кнопки "Reset App State"

