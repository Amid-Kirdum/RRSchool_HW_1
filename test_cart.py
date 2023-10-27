# **Cart**
# 1. Add item to cart from catalog

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Passed
def test_add_to_cart_from_catalog():
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

#FAILED
def test_remove_from_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    time.sleep(3)

    add_to_cart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    time.sleep(3)

    cart_badge_before = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text

    time.sleep(3)

    shopping_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart.click()

    time.sleep(3)

    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button.click()

    time.sleep(3)
    cart_badge_after = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a/span')

    assert int(cart_badge_before) != int(cart_badge_after)

    driver.quit()

    # 3. Add an item to the cart via the cart item

#PASSED
def test_add_to_cart_from_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    # text_before = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']").text   #CSS_Selector
    text_before = driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]").text  # XPATH
    # text_before = driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Bike Light')]").text  # XPATH

    time.sleep(3)

    cart_item = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name "]')
    cart_item.click()

    btn_add_to_cart = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    btn_add_to_cart.click()

    shopping_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart.click()

    # text_after = driver.find_element(By.CSS_SELECTOR,"a[id='item_4_title_link'] > div[class='inventory_item_name']").text #CSS_Selector
    text_after = driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]").text  # XPATH

    assert (text_before == text_after)

    driver.quit()

    # 4. Removing an item from cart via the cart item

#FAILED
def test_remove_from_cart_via_cart_item():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    time.sleep(3)

    cart_item = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
    cart_item.click()

    time.sleep(3)

    btn_add_to_cart = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    btn_add_to_cart.click()

    time.sleep(3)

    cart_with_item = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span]')

    time.sleep(3)

    # btn_remove = driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    # btn_remove.click()

    cart_without_item = driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]').text

    assert (cart_with_item) != (cart_without_item)

    driver.quit()