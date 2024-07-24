import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_object.base_method import Base_Method as BM

class Main_Page:
    def __init__(self, browser) -> None:
        self.browser = browser

    def checking_the_shopping_cart(self):
        span_elem = BM(browser=self.browser).text_elem_by_xpath(selector='//*[@id="header-cart"]/div/button')
        if span_elem.text != '0 item(s) - $0.00':
            raise ValueError(f'Корзина уже заполнена: {span_elem.text}')
    
    def adding_product(self, index = 1):
        elem = self.browser.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div[{index}]/div/div[2]/form/div/button[1]') #Записываем элемент в переменную
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem) # Прокручиваем к элементу
        time.sleep(2)
        elem.click()
        return index

    def scrolling_the_page_to_the_shopping_cart(self):
        BM(browser=self.browser).scrolling_to_elem
    
    def check_cart(self, index):
        span_elem = self.browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
        if index == 1:
            if span_elem.text != '1 item(s) - $602.00':
                raise ValueError(f'Корзина уже заполнена: {span_elem.text}')
        elif index == 2:
            if span_elem.text != '1 item(s) - $123.20':
                raise ValueError(f'Корзина уже заполнена: {span_elem.text}')
            
    def check_5_elem_on_main_page(self):
        BM(browser=self.browser).element_visibility(selector='//*[@id="logo"]/a/img')
        BM(browser=self.browser).element_clickable(selector='//*[@id="narbar-menu"]/ul/li[6]')
        BM(browser=self.browser).element_visibility(selector='//*[@id="content"]/div[2]/div[3]/div/div[1]')
        BM(browser=self.browser).not_element_visibility(selector='//*[@id="test"]')
        BM(browser=self.browser).element_clickable(selector='//*[@id="search"]/input[3]')

    def change_currency_to_dollar(self):
        BM(browser=self.browser).click_to_element(selector='//*[@id="form-currency"]/div/a')
        BM(browser=self.browser).click_to_element(selector='//*[@id="form-currency"]/div/ul/li[3]/a')
    
    def check_elem_take_dollars(self, selector):
        """Проверяет на главной странице что у элемента поменялась валюта на доллары"""
        element = self.browser.find_element(By.XPATH, selector) #Записываем элемент в переменную
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element) # Прокручиваем к элементу
        time.sleep(2)

        if element.text != '1 item(s) - $602.00': # Проверяю что цена в долларах
            raise ValueError(f'Цена не изменилась на доллары на товаре: {element.text}')

    
