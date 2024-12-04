from .base import BasePage
from locators import Mainsbis, Downloads, Tenzor
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os


class ContactPage(BasePage):
    '''В данном классе описаны действия'''

    def go_to_contacts(self):
        '''Переходит в контакты'''
        self.find_element(Mainsbis.CONTACT, time=5).click()
        sleep(1)
        self.find_element(Mainsbis.MORE_CONTACTS, time=5).click()

    def click_banner(self):
        '''Кликает на баннер'''
        self.find_element(Mainsbis.BANNER_TENZOR, time=5).click()

    def check_findpeople(self):
        '''Ищет блок Сила в людях'''
        people_block = self.find_element(Tenzor.PEOPLE_BLOCK, time=5)
        assert people_block and 'Сила в людях' in people_block.text, 'нет блока'

    def go_details(self):
        '''переходит в раздел About'''
        news = self.find_element(Tenzor.NEWS, time=5)
        ActionChains(self.driver).move_to_element(news).perform()  # пролистать до новостей
        self.find_element(Tenzor.ABOUT, time=5).click()

    def check_photo(self):
        '''получает размеры картинок и сравнивает их'''
        photos = self.find_elements(Tenzor.PHOTO, time=5)
        widths = [int(i.get_attribute("width")) for i in photos]
        height = [int(i.get_attribute("height")) for i in photos]
        result = True if sum(widths) / len(widths) == widths[1] and sum(height) / len(height) == height[1] else False
        assert result, 'размеры не совпадают'

    def get_area(self) -> tuple:
        '''получает регион и список партнеров, возвращает кортеж из 2 элементов'''
        area = self.find_element(Mainsbis.AREA).text
        partners = self.find_elements(Mainsbis.PARTNERS)
        data = area, partners
        return data

    def check_area(self, area='Ханты-Мансийский АО-Югра'):
        info = self.get_area()
        assert info[0] == area and len(info[1]) > 1

    def change_region(self):
        '''Меняет регион на Камчатский край'''
        self.find_element(Mainsbis.AREA).click()
        vvod = self.find_element(Mainsbis.STROKA_REGION)
        vvod.click()
        vvod.send_keys('Камчатский')
        sleep(3)
        self.find_element(Mainsbis.REGION).click()
        sleep(3)

    def download(self) -> float:
        '''Скачивает плагин на ПК и возвращает объем, указанный на сайте'''
        icon = self.find_element(Downloads.ICONS)
        ActionChains(self.driver).move_to_element(icon).perform()
        self.find_element(Downloads.DOWNLOAD).click()
        download = self.find_element(Downloads.WEBINST)
        digits = [l for l in download.text if l.isdigit() or l == '.']
        razm = float(''.join(digits))
        download.click()
        return razm

    def checkrazm(self, razm: float, path: str = "C:/Users/User/Downloads/sbisplugin-setup-web.exe"):
        '''Проверяет размер файла'''
        razm_skach = round(os.path.getsize(path) / 1024 / 1024, 2)
        assert razm_skach == razm, 'скачал не то'
