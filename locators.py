from selenium.webdriver.common.by import By


class Mainsbis:
    CONTACT = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu")
    MORE_CONTACTS = (By.CSS_SELECTOR, ".sbisru-link")
    BANNER_TENZOR = (By.CSS_SELECTOR, ".sbisru-Contacts__border-left--border-xm>.sbisru-Contacts__logo-tensor")
    AREA = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text")
    PARTNERS = (By.CSS_SELECTOR, ".sbisru-Contacts-List__name")
    REGION = (By.CSS_SELECTOR, ".sbis_ru-link")
    STROKA_REGION = (By.CSS_SELECTOR, ".controls-Search__nativeField_caretEmpty")


class Downloads:
    ICONS = (By.CSS_SELECTOR, ".sbisru-Footer__address-icon")
    DOWNLOAD = (By.CSS_SELECTOR, "[href='/download']")
    WEBINST = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-loadLink__link")


class Tenzor:
    PEOPLE_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg")
    NEWS = (By.CSS_SELECTOR, "[class='nl-LastCovers__header_title']")
    ABOUT = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg [class='tensor_ru-Index__card-text'] a")
    PHOTO = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image")
