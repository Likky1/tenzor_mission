from pages.contacts import ContactPage
from pages.main import MainPage
import pytest


@pytest.mark.usefixtures('browser')
class TestTask1:
    '''В данном классе описаны тесты первого задания'''

    def setup_method(self):
        self.contpage = ContactPage(self.driver)
        self.mainpage = MainPage(self.driver)
        self.mainpage.go_to_mainsite()

    def teardown_method(self):
        '''Закрывает вторую вкладку браузера'''
        if len(self.contpage.driver.window_handles) > 1:
            self.contpage.go_to_window(handle_num=1)
            self.contpage.driver.close()
            self.contpage.go_to_window(handle_num=0)

    def test_scenary_1(self):
        self.contpage.go_to_contacts()
        self.contpage.click_banner()
        self.contpage.go_to_window(1)
        self.contpage.check_findpeople()
        self.contpage.go_details()
        assert self.contpage.get_link() == 'https://tensor.ru/about', 'не та ссылка'
        self.contpage.check_photo()

    def test_scenary_2(self):
        self.contpage.go_to_contacts()
        infoHMAO = self.contpage.get_area()
        self.contpage.check_area()
        self.contpage.change_region()
        infoKK = self.contpage.get_area()
        requirements = {'не совпадают партнеры/n': infoHMAO[1] != infoKK[1],
                        'название региона/n': infoKK[0] == 'Камчатский край',
                        'изменилась ссылка/n': '41-kamchatskij-kraj' in self.contpage.get_link(),
                        'изменилось название страницы/n': 'Камчатский край' in self.contpage.get_title()
                        }
        errors = ''
        for i in requirements:
            if requirements[i] == False:
                errors += i
        assert not (errors), errors

    def test_scenary_3(self):
        size = self.contpage.download()
        self.contpage.checkrazm(size)
