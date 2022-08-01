from selenium.webdriver.common.by import By
from selenium import webdriver


class TestConstructor:

    def test_click_to_tab2_success(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        # tab - раздел "Соусы" в конструкторе
        tab = driver.find_element(By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]")
        tab.click()

        # Получение классов в разделах с ингридиентами
        classes = tab.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in classes

        driver.quit()

    def test_click_to_tab3_success(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переход в раздел "Соусы" в конструкторе
        driver.find_element(By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]").click()
        # tab - раздел "Начинки" в конструкторе
        tab = driver.find_element(By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[3]")
        tab.click()

        # Получение классов в разделе с ингредиентами
        classes = tab.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in classes

        driver.quit()

    def test_click_to_tab1_success(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переход в раздел "Начинки" в конструкторе
        driver.find_element(By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[3]").click()

        # tab - раздел "Булки" в конструкторе
        tab = driver.find_element(By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[1]")
        tab.click()

        # classes - получение списка классов в разделе с ингредиентами
        classes = tab.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in classes

        driver.quit()
