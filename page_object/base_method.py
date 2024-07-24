import time
import randominfo
import logging 

from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_Method:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.logger = browser.logger
    
    def text_elem_by_xpath(self, selector):
        """Вовзращает текст элемента по XPATH!"""
        self.logger.debug("Возвращаю текст элемента по селектору: %s" % (selector))
        return self.browser.find_element(By.XPATH, selector).text
    
    def scrolling_to_elem(self, selector):
        """Прокручивает до элемента по XPATH!"""
        elem = self.browser.find_element(By.XPATH, selector) #Записываем элемент в переменную
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem) # Прокручиваем к корзине
        time.sleep(2)
        return elem
    
    def element_visibility(self, selector, wait_time=1):
        """Проверяет что элемент виден на странице по XPATH"""
        self.logger.debug("Проверяю что элемент виден на странице: %s" % (selector))
        return WebDriverWait(self.browser, wait_time).until(EC.visibility_of_element_located((By.XPATH, selector)))
    
    def not_element_visibility(self, selector, wait_time=1):
        """Проверяет что элемент НЕ виден на странице по XPATH"""
        self.logger.debug("Проверяю что элемент на странице не виден: %s" % (selector))
        return WebDriverWait(self.browser, wait_time).until_not(EC.visibility_of_element_located((By.XPATH, selector)))

    def element_clickable(self, selector, wait_time=1):
        """Проверяет что элемент кликабельный на странице по XPATH"""
        self.logger.debug("Проверяю что элемент на странице кликабельный: %s" % (selector))
        return WebDriverWait(self.browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, selector)))
    
    def add_to_the_link_in_the_browser(self, link_continuation):
        """К текущему линк-у добавляет его продолжение"""
        self.logger.debug("Добавляю к текущему линку, продолжение: %s" % (link_continuation))
        self.browser.get(self.browser.current_url + link_continuation)

    def comparing_the_current_address(self, address):
        """Проверяет текущий адресс с пользовательским значением"""
        self.logger.debug("Проверяю текущий адресс с пользовательским значением: %s" % (address))
        test_check_url = self.browser.current_url
        if test_check_url != address:
            raise ValueError(f'Адреса не равны: {test_check_url}')
        
    def send_text_to_elem_by_xpath(self, selector, text_for_send, wait_time=1):
        """Вписывает текст в элемент типа input по XPATH"""
        self.logger.debug("Вписываю %s в элемент: %s" % (text_for_send, selector))
        elem = self.browser.find_element(By.XPATH, selector) #Записываем элемент в переменную
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem) # Прокручиваем к элементу
        time.sleep(3)
        WebDriverWait(self.browser, wait_time).until(EC.visibility_of_element_located((By.XPATH, selector))).send_keys(text_for_send)
    
    def click_to_element(self, selector, wait_time=2):
        """Проверяет что элемент кликабельный и нажимает на него"""
        self.logger.debug("Проверяю кликабельность элемента: %s" % (selector))
        elem = self.browser.find_element(By.XPATH, selector) #Записываем элемент в переменную
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem) # Прокручиваем к элементу
        WebDriverWait(self.browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, selector))).click()

    def get_link(self, link):
        self.logger.debug("Opening url: %s" %(link))
        self.browser.get(link)
        
    def check_text_and_compariso(self, selector, text_comparison='Your Account Has Been Created!'):
        self.logger.debug("Проверяю регистрацию: %s" % (text_comparison))
        text_elem = Base_Method(browser=self.browser).text_elem_by_xpath(selector=selector).text
        if text_elem != text_comparison:
            raise ValueError(f'Регистрация не успешна')