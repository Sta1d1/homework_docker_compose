from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from page_object.main_page import Main_Page as MP
from page_object.base_method import Base_Method as BM
from page_object.category_product_page import Category_Page as CP


def test_switch_currency(browser: Remote):
    """Меняю валюту и проверяю на главное странице что она изменилась"""
    MP(browser=browser).change_currency_to_dollar()
    BM(browser=browser).add_to_the_link_in_the_browser(link_continuation='/index.php?route=product/category&language=en-gb&path=18')
    time.sleep(5)
    BM(browser=browser).scrolling_to_elem(selector='//*[@id="product-list"]/div[3]/div/div[2]/div/div/span[1]')
    CP(browser=browser).checking_that_the_price_of_the_item_is_in_dollars(selector='//*[@id="product-list"]/div[3]/div/div[2]/div/div/span[1]')
    CP(browser=browser).checking_that_the_price_of_the_item_is_in_dollars(selector='//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]')

    




    