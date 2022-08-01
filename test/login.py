from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class TestLogin:

    def test_from_main_page_success(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Кнопка входа на главной странице
        driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').click()

        # Инпут для ввода логина
        driver.find_element(By.NAME, "name").send_keys("yulialukonina1988@yandex.ru")
        # Инпут для ввода пароля
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        # Кнопка входа
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        time.sleep(1)

        # Кнопка "Оформить заказ" на главной странице
        assert driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').text == "Оформить заказ"

        driver.quit()

    def test_from_account_page_success(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Кнопка входа в личный кабинет на главной странице
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

        # Инпут для ввода логина
        driver.find_element(By.NAME, "name").send_keys("yulialukonina1988@yandex.ru")
        # Инпут для ввода пароля
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        # Кнопка входа
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        time.sleep(1)

        # Кнопка "Оформить заказ" на главной странице
        assert driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').text == "Оформить заказ"

        driver.quit()

    def test_from_registration_page_success(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        # Кнопка входа на странице регистрации
        driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

        # Инпут для ввода логина
        driver.find_element(By.NAME, "name").send_keys("yulialukonina1988@yandex.ru")
        # Инпут для ввода пароля
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        # Кнопка входа
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        time.sleep(1)

        # Кнопка "Оформить заказ" на главной странице
        assert driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').text == "Оформить заказ"

        driver.quit()

    def test_from_reset_password_page_success(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        # Кнопка входа на странице восстановления пароля
        driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

        # Инпут для ввода логина
        driver.find_element(By.NAME, "name").send_keys("yulialukonina1988@yandex.ru")
        # Инпут для ввода пароля
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        # Кнопка входа
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        time.sleep(1)

        # Кнопка "Оформить заказ" на главной странице
        assert driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').text == "Оформить заказ"

        driver.quit()
