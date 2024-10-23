from selenium.webdriver.common.by import By
from pages.simple_page import SimpeButtonPage

def test_button1_exist(browser):
    #создаем сессию работы со страницей
    simple_page = SimpeButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()

def test_button1_clicked(browser):
    simple_page = SimpeButtonPage(browser)
    simple_page.open()
    simple_page.click_button()
    assert "Submitted" == simple_page.result_text

