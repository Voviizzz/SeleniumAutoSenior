from selenium import webdriver

import pytest


#Данной фикстурой настраиваем браузер
@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


