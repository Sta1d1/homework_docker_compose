import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_object.base_method import Base_Method as BM

class Category_Page:
    def __init__(self, browser) -> None:
        self.browser = browser
    
    def checking_that_the_price_of_the_item_is_in_dollars(self, selector):
        """Прокручивает до элемента и проверяет что его цена в долларах"""
        element = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located((By.XPATH, 'selector'))) #Записываем элемент в переменную
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element) # Прокручиваем к элементу
        time.sleep(2)
        if element.text[0] != '$': # Проверяю что цена в долларах
            raise ValueError(f'Цена не изменилась на доллары на товаре: {element.text}')