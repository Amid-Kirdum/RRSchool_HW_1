# **Cart**
# 1. Add item to cart from catalog

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

    add_to_cart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    shopping_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart.click()

    time.sleep(5)
    # text_after = driver.find_element(By.CSS_SELECTOR,"a[id='item_4_title_link'] > div[class='inventory_item_name']").text #CSS_Selector
    text_after = driver.find_element(By.XPATH,"//div[contains(text(),'Sauce Labs Backpack')]").text       # XPATH

    time.sleep(4)
    assert(text_before == text_after)

    driver.quit()

    # 2. Removing an item from the cart via the cart
def test_remove_from_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    cart_badge_before = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]').text
    print(cart_badge_before)

    time.sleep(3)
    shopping_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart.click()

    time.sleep(3)

    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button.click()

    time.sleep(3)
    cart_badge_after = driver.find_element(By.XPATH,'')

    # 3. Добавление товара в корзину из карточки товара
    # 4. Удаление товара из корзины через карточку товара
    #
