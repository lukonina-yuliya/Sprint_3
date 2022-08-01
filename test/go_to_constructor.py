from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class TestGoToConstructor:

    def test_click_to_constructor_go_constructor(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Кнопка входа на главной странице
        button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
        button.click()

        # Инпут для ввода логина
        driver.find_element(By.NAME, "name").send_keys("yulialukonina1988@yandex.ru")
        # Инпут для ввода пароля
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        # Кнопка входа
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        time.sleep(1)

        # Кнопка перехода в личный кабинет на главной странице
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "Account_contentBox__2CPm3"))
        )

        # Кнопка "Конструктор" в шапке сайте
        driver.find_element(By.CLASS_NAME, 'AppHeader_header__link__3D_hX').click()
        # label - заголовок "Соберите бургер" на главной странице
        label = driver.find_element(By.CLASS_NAME, 'text_type_main-large')
        assert label.text == 'Соберите бургер'

        driver.quit()

    def test_click_to_logo_go_constructor(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Кнопка входа на главной странице
        button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
        button.click()

        # Инпут для ввода логина
        driver.find_element(By.NAME, "name").send_keys("yulialukonina1988@yandex.ru")
        # Инпут для ввода пароля
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        # Кнопка входа
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        time.sleep(1)

        # Кнопка перехода в личный кабинет на главной странице
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "Account_contentBox__2CPm3"))
        )

        # Логотип в шапке сайта
        driver.find_element(By.CLASS_NAME, 'AppHeader_header__logo__2D0X2').click()
        # label - заголовок "Соберите бургер" на главной странице
        assert driver.find_element(By.CLASS_NAME, 'text_type_main-large').text == 'Соберите бургер'

        driver.quit()
