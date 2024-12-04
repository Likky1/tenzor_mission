import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
