from selenium.webdriver.common.by import By

from conftest import browser
from .base_page import BasePage


button_selector = (By.ID, 'submit-id-submit')
result_selector = (By.ID, 'result')

class SimpeButtonPage(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def button(self):
        return self.find(button_selector)

    def result(self):
        return self.find(result_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def click_button(self):
        self.button().click()

    @property
    def result_text(self):
        return self.result().text

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/button/simple")

