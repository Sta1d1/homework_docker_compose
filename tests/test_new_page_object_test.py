import time
import randominfo

from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.main_page import Main_Page as MP
from page_object.base_method import Base_Method as BM
from page_object.category_product_page import Category_Page as CP
from page_object.admin_page import Admin_Page as AP

def test_add_new_product_in_admin_panel(browser: Remote):
    AP(browser=browser).go_to_admin_page()
    AP(browser=browser).login_admin()
    AP(browser=browser).go_to_my_product()
    AP(browser=browser).add_new_product()

def test_dell_product_in_admin_panel(browser: Remote):
    AP(browser=browser).go_to_admin_page()
    AP(browser=browser).login_admin()
    AP(browser=browser).go_to_my_product()
    AP(browser=browser).dell_product()

def test_new_user_registration(browser: Remote):
    BM(browser=browser).get_link(link='http://localhost/index.php?route=account/register')
    BM(browser=browser).send_text_to_elem_by_xpath(selector='//*[@id="input-firstname"]', text_for_send=randominfo.get_first_name)
    BM(browser=browser).send_text_to_elem_by_xpath(selector='//*[@id="input-lastname"]', text_for_send=randominfo.get_last_name)
    BM(browser=browser).send_text_to_elem_by_xpath(selector='//*[@id="input-email"]', text_for_send=randominfo.get_email)
    BM(browser=browser).send_text_to_elem_by_xpath(selector='//*[@id="input-password"]', text_for_send=randominfo.random_password)
    BM(browser=browser).click_to_element(selector='//*[@id="form-register"]/div/div/input')
    BM(browser=browser).click_to_element(selector='//*[@id="form-register"]/div/button')
    BM(browser=browser).text_elem_by_xpath(selector='//*[@id="content"]/h1')
    time.sleep(5)
    BM(browser=browser).check_text_and_compariso(selector='//*[@id="content"]/h1')