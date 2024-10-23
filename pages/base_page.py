#Абстрактный класс, который подходит ко всем страницам
from conftest import browser


class BasePage:
    def __init__(self, browser):
        self.browser = browser

#для упрощения поиска элементов
    def find(self, args):
        return self.browser.find_element(*args)

#    def click(self):
#        self.browser.find().click()

