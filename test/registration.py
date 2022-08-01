from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class TestRegistration:

    def test_registration_success(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # email - генерация логина для регистрации
        email = "lukonina_" + str(time.time())+"@yandex.ru"
        # Инпут для ввода имени
        driver.find_element(By.XPATH, './/form/fieldset[1]/div/div/input').send_keys("TestUser")
        # Инпут для ввода логина
        driver.find_element(By.XPATH, './/form/fieldset[2]/div/div/input').send_keys(email)
        # Инпут для ввода пароля
        driver.find_element(By.XPATH, ".//form/fieldset[3]/div/div/input").send_keys("123456789")
        # Кнопка регистрации
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        time.sleep(1)

        # Инпут для ввода логина
        driver.find_element(By.NAME, "name").send_keys(email)
        # Инпут для ввода пароля
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        # Кнопка входа
        button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
        button.click()
        time.sleep(1)

        # Кнопка "Оформить заказ" на главной странице
        assert driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').text == "Оформить заказ"

        driver.quit()

    def test_empty_name_no_registration(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # email - генерация логина для регистрации
        email = "lukonina_" + str(time.time()) + "@yandex.ru"
        # Инпут для ввода имени
        driver.find_element(By.XPATH, './/form/fieldset[1]/div/div/input').send_keys("")
        # Инпут для ввода логина
        driver.find_element(By.XPATH, './/form/fieldset[2]/div/div/input').send_keys(email)
        # Инпут для ввода пароля
        driver.find_element(By.XPATH, ".//form/fieldset[3]/div/div/input").send_keys("123456789")
        # Кнопка регистрации
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

        driver.quit()

    def test_short_password_error(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # email - генерация логина для регистрации
        email = "lukonina_" + str(time.time()) + "@yandex.ru"
        # Инпут для ввода имени
        driver.find_element(By.XPATH, './/form/fieldset[1]/div/div/input').send_keys("")
        # Инпут для ввода логина
        driver.find_element(By.XPATH, './/form/fieldset[2]/div/div/input').send_keys(email)
        # Инпут для ввода пароля
        driver.find_element(By.XPATH, ".//form/fieldset[3]/div/div/input").send_keys("12345")
        # Кнопка регистрации
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        time.sleep(1)

        # Инпут для ввода пароля
        input_div = driver.find_element(By.XPATH, ".//form/fieldset[3]/div/div")
        # Получение классов инпута для ввода пароля
        classes = input_div.get_attribute('class')

        assert 'input_status_error' in classes

        driver.quit()
