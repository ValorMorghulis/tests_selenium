import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture()
def driver(request):
    city = "Москва"
    web_driver = WebDriver(executable_path='C://python//chromedriver.exe')
    web_driver.implicitly_wait(3)
    yield web_driver
    web_driver.close()
