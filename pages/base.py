from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    '''В данном классе описаны основные действия, осуществляемые в браузере'''

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=20):
        '''Возвращает элемент по локатору либо ошибку
            :param locator: локатор поиска в веб-документе
            :param time: время на поиск локатора, по истечению времени - ошибка'''
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        '''Возвращает список элементов по локатору либо ошибку
                :param locator: локатор поиска в веб-документе
                :param time: время на поиск локатора, по истечению времени - ошибка'''
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_window(self, handle_num):
        '''Переходит на указанную вкладку браузера
        :param handle_num: индекс вкладки'''
        return self.driver.switch_to.window(self.driver.window_handles[handle_num])

    def get_link(self):
        '''возвращает адрес ссылки активной вкладки'''
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
