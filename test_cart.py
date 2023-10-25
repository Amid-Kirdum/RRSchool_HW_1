# **Корзина**
# 1. Добавление товара в корзину через каталог

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    time.sleep(4)
    # text_before = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']").text   #CSS_Selector
    text_before = driver.find_element(By.XPATH,"//div[contains(text(),'Sauce Labs Backpack')]").text  # XPATH

    addToCart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    addToCart_button.click()

    shopping_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart.click()

    time.sleep(5)
    # text_after = driver.find_element(By.CSS_SELECTOR,"a[id='item_4_title_link'] > div[class='inventory_item_name']").text #CSS_Selector
    text_after = driver.find_element(By.XPATH,"//div[contains(text(),'Sauce Labs Backpack')]").text       # XPATH

    time.sleep(4)
    assert(text_before == text_after)

    # 2. Удаление товара из корзины через корзину
def test_remove_from_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    addToCart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    addToCart_button.click()



    shopping_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart.click()

    # 3. Добавление товара в корзину из карточки товара
    # 4. Удаление товара из корзины через карточку товара
    #
