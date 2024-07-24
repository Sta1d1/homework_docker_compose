import pytest
import logging
import datetime
import allure
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="ch", choices=["ya", "ch", "ff"]
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--yadriver", action="store_true", default="/home"
    )
    parser.addoption(
        "--url", default="http://vk.com/"
    )
    parser.addoption(
        "--log_level", default="INFO"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    test_url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("Test %s startet at %s" % (request.node.name, datetime.datetime.now()))

    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON)



    if browser_name == "ya":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        options.binary_location = "/usr/bin/yandex-browser"
        service = Service(executable_path=yadriver)
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "ch":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        browser = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless_mode:
            options.add_argument("--headless")
        browser = webdriver.Firefox(service=FFService(), options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    browser.logger = logger
    logger.info("Browser %s started" % browser)

    browser.maximize_window()
    browser.get(test_url)
    
    yield browser


    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=browser.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            name="page_source",
            body=browser.page_source,
            attachment_type=allure.attachment_type.HTML
        )

    browser.close()
    logger.info("Test %s finished at %s" % (request.node.name, datetime.datetime.now()))