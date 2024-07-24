import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_object.base_method import Base_Method as BM

class Admin_Page:
    def __init__(self, browser) -> None:
        self.browser = browser
    
    def check_elem_on_page(self):
        """Проверка элементов на странице авторизации под администратором"""
        BM(browser=self.browser).element_visibility(selector='//*[@id="header"]/div/a')
        BM(browser=self.browser).element_clickable(selector='//*[@id="input-username"]')
        BM(browser=self.browser).element_clickable(selector='//*[@id="input-password"]')
        BM(browser=self.browser).element_clickable(selector='//*[@id="form-login"]/div[3]/button')
    
    def go_to_admin_page(self):
        """Переход на страницу аминистратора с главной страницы"""
        BM(browser=self.browser).add_to_the_link_in_the_browser(link_continuation='admin/')
        BM(browser=self.browser).comparing_the_current_address(address='http://localhost/admin/')
    
    def login_admin(self):
        """Авторизация на странице администратора"""
        BM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-username"]',text_for_send='admin')
        BM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-password"]',text_for_send='admin')
        BM(browser=self.browser).click_to_element(selector='//*[@id="form-login"]/div[3]/button')
        BM(browser=self.browser).click_to_element(selector='//*[@id="modal-security"]/div/div/div[1]/button')
        BM(browser=self.browser).element_visibility(selector='//*[@id="content"]/div[2]/div[2]/div[2]/div/div[1]')
    
    def logout_admin(self):
        """Выход из панели администратора с основной страницы администратора"""
        BM(browser=self.browser).click_to_element(selector='//*[@id="nav-logout"]')
        time.sleep(3)
        BM(browser=self.browser).comparing_the_current_address(address='http://localhost/admin/index.php?route=common/login')
    
    def go_to_my_product(self):
        """Переход с главной страницы аминистратора к товарам администратора"""
        BM(browser=self.browser).click_to_element(selector='//*[@id="menu-catalog"]')
        BM(browser=self.browser).click_to_element(selector='//*[@id="collapse-1"]/li[2]')

    def add_new_product(self):
        """Добавление нового продукта в панеле администратора из вкладки 'Products'"""
        BM(browser=self.browser).click_to_element(selector='//*[@id="content"]/div[1]/div/div/a')
        BM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-name-1"]', text_for_send='New Product')
        BM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-meta-title-1"]', text_for_send='New Product')
        BM(browser=self.browser).send_text_to_elem_by_xpath(selector='/html/body', text_for_send='Тестовое добавление нового товара')
        BM(browser=self.browser).click_to_element(selector='//*[@id="form-product"]/ul/li[2]/a')
        BM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-model"]', text_for_send='Test_model')
        BM(browser=self.browser).click_to_element(selector='//*[@id="content"]/div[1]//button')
    
    def dell_product(self):
        BM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-name"]', text_for_send='New Product')
        BM(browser=self.browser).click_to_element(selector='//*[@id="button-filter"]')
        time.sleep(3)
        BM(browser=self.browser).click_to_element(selector='//*[@id="form-product"]/div[1]/table/tbody/tr/td[1]/input')
        pyautogui.press('enter')
        