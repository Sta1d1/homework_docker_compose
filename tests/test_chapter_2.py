from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.base_method import Base_Method as BM
from page_object.main_page import Main_Page as MP
from page_object.admin_page import Admin_Page as AP
from page_object.register_page import Register_Page as RP


def test_main_page(browser): 
    """Проверка элементов на главной странице opencart"""
    MP(browser=browser).check_5_elem_on_main_page()
    
   
def test_catalog(browser):
    """Проверка элементов на странице <Каталог>"""
    BM(browser=browser).add_to_the_link_in_the_browser(link_continuation='index.php?route=product/category&language=en-gb&path=25_28')
    BM(browser=browser).element_visibility(selector='//*[@id="logo"]')
    BM(browser=browser).comparing_the_current_address(address='http://localhost/index.php?route=product/category&language=en-gb&path=25_28')
    BM(browser=browser).element_clickable(selector='//*[@id="header-cart"]/div/button')
    BM(browser=browser).element_clickable(selector='//*[@id="product-list"]/div[2]/div/div[2]/div/h4')
    BM(browser=browser).element_clickable(selector='//*[@id="search"]/input[3]')

def test_product_cart(browser):
    """Проверка элементов на странице <Карточка товара>"""
    BM(browser=browser).add_to_the_link_in_the_browser(link_continuation='index.php?route=product/product&language=en-gb&product_id=49&path=57')
    BM(browser=browser).comparing_the_current_address(address='http://localhost/index.php?route=product/product&language=en-gb&product_id=49&path=57')
    BM(browser=browser).element_visibility(selector='//*[@id="header-cart"]/div/button')
    BM(browser=browser).element_clickable(selector='//*[@id="button-cart"]')
    BM(browser=browser).element_visibility(selector='//*[@id="content"]/ul/li[2]/a')
    BM(browser=browser).not_element_visibility(selector='//*[@id="test"]/input[3]')


def test_administration_page(browser):
    """Проверка элементов на странице <админки>"""
    AP(browser=browser).go_to_admin_page()
    AP(browser=browser).check_elem_on_page()
    
    
def test_register_page(browser):
    """Проверка элементов на странице <регистрации>"""
    BM(browser=browser).add_to_the_link_in_the_browser(link_continuation='index.php?route=account/register')
    BM(browser=browser).comparing_the_current_address(address='http://localhost/index.php?route=account/register')
    RP(browser=browser).check_elem_on_page()
    


    