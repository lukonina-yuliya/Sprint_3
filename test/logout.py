from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class TestLogout:

    def test_logout_from_account_success(self):
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

        # Кнопка входа в личный кабинет на главной странице
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "Account_contentBox__2CPm3"))
        )

        # Кнопка выхода из аккаунта в личном кабинете
        driver.find_element(By.CLASS_NAME, 'Account_button__14Yp3').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "Auth_link__1fOlj"))
        )

        # Кнопка входа на главной странице
        assert driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').text == 'Войти'

        driver.quit()
