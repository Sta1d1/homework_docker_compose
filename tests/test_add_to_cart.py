import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.main_page import Main_Page as MP


def test_add_to_cart(browser: Remote):
    """Добавляю случайный товар в корзину и проверяю что он появился в корзине"""
    MP(browser).checking_the_shopping_cart()
    index = MP(browser).adding_product()
    MP(browser).scrolling_the_page_to_the_shopping_cart()
    MP(browser).check_cart(index=index)

    
    