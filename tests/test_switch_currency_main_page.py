import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.main_page import Main_Page as MP
from page_object.base_method import Base_Method as BM
from page_object.category_product_page import Category_Page as CP


def test_switch_currency(browser: Remote):
    """Меняю валюту и проверяю на главное странице что она изменилась"""
    MP(browser=browser).change_currency_to_dollar()
    MP(browser=browser).check_elem_take_dollars(selector='//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
    BM(browser=browser).click_to_element(selector='//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')
    BM(browser=browser).scrolling_to_elem(selector='//*[@id="header-cart"]/div/button')
    time.sleep(2)
    MP(browser=browser).check_elem_take_dollars(selector='//*[@id="header-cart"]/div/button')
    
