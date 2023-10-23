# # Домашнее задание к первому уроку
#
# **Необходимо написать автотесты для сайта saucedemo:**
# ***Ссылка на сайт: https://www.saucedemo.com/***
#
# Функционал, который необходимо покрыть автотестами:
#
# **Авторизация**
# 1. Авторизация используя корректные данные (standard_user, secret_sauce)
from cgitb import text

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
def test_auth_valid():
    driver.get ("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH,'//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

# 2. Авторизация используя некорректные данные (user, user)
def test_auth_invalid():
    driver.get ("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH,'//input[@id="password"]')
    password_field.send_keys('standard_user')

    login_button = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
#
# **Корзина**
# 1. Добавление товара в корзину через каталог
def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

    text_before = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']").text   #CSS_Selector
    # text_before = driver.find_element(By.XPATH,"//div[contains(text(),'Sauce Labs Backpack')]").text  # XPATH

    addToCart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    addToCart_button.click()

    shopping_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart.click()

    text_after = driver.find_element(By.CSS_SELECTOR,"a[id='item_4_title_link'] > div[class='inventory_item_name']").text #CSS_Selector
    # text_after = driver.find_element(By.XPATH,"//div[contains(text(),'Sauce Labs Backpack')]").text       # XPATH

    assert(text_before == text_after)

# 2. Удаление товара из корзины через корзину


# 3. Добавление товара в корзину из карточки товара
# 4. Удаление товара из корзины через карточку товара
#
# **Карточка товара**
# 1. Успешный переход к карточке товара после клика на картинку товара
# 2. Успешный переход к карточке товара после клика на название товара
#
# **Оформление заказа**
# 1. Оформление заказа используя корректные данные
#
# **Фильтр**
# 1. Проверка работоспособности фильтра (A to Z)
# 2. Проверка работоспособности фильтра (Z to A)
# 3. Проверка работоспособности фильтра (low to high)
# 4. Проверка работоспособности фильтра (high to low)
#
# **Бургер меню**
# 1. Выход из системы
# 2. Проверка работоспособности кнопки "About" в меню
# 3. Проверка работоспособности кнопки "Reset App State"
#
#
#
# Чек лист достаточно примерный. Чуть позже во время практики над основным проектом мы сможем поработать с качественной документацией.
#
# Основная суть данного задания - попробовать Selenium и Pytest на практике.
#
# Для выполнения задания нужно создать новый репозиторий и написать некоторое количество автотестов.