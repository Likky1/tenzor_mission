from .base import BasePage


class MainPage(BasePage):
    base_url = "https://sbis.ru/"

    def go_to_mainsite(self):
        '''Переходит на главную страницу'''
        self.driver.get(self.base_url)
