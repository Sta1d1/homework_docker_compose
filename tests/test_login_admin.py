from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.base_method import Base_Method as BM
from page_object.main_page import Main_Page as MP
from page_object.admin_page import Admin_Page as AP
from page_object.register_page import Register_Page as RP

def test_authorization_logout(browser):
    """Вход и выход в админку с проверкой"""
    AP(browser=browser).go_to_admin_page()
    AP(browser=browser).login_admin()
    AP(browser=browser).logout_admin()
    
    