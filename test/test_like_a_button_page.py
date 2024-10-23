from selenium.webdriver.common.by import By
from pages.like_a_button_page import LikeAButtonPage


def test_button2_exist(browser):
    #опять создаем сессию
    like_a_button = LikeAButtonPage(browser)
    like_a_button.open()
    assert like_a_button.button_is_displayed

def test_button2_clicked(browser):
    like_a_button = LikeAButtonPage(browser)
    like_a_button.open()
    like_a_button.button.button_click()
    assert "Submitted" == like_a_button.result_text