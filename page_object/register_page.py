import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_object.base_method import Base_Method as BM

class Register_Page:
    def __init__(self, browser) -> None:
        self.browser = browser
    
    def check_elem_on_page(self):
        BM(browser=self.browser).element_visibility(selector='//*[@id="input-firstname"]')
        BM(browser=self.browser).element_visibility(selector='//*[@id="input-password"]')
        BM(browser=self.browser).element_visibility(selector='//*[@id="account-register"]/ul/li[3]/a')
        BM(browser=self.browser).element_clickable(selector='//*[@id="logo"]')