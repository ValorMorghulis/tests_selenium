from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons.types import Severity
import allure


@allure.title('Проверяем смену города на Новосибирск и сохранение выбора после перезагрузки страницы')
@allure.severity(Severity.NORMAL)
def test_lamoda_change_city():
    driver = WebDriver(executable_path='C://python//chromedriver.exe')
    driver.implicitly_wait(10)
    city_name = "г Новосибирск"
    with allure.step('Открываем страницу сайта Ламода'):
        driver.get('https://lamoda.ru')

    with allure.step('Нажимаем на кнопку выбора региона доставки'):
        search_button = driver.find_element_by_xpath('//span[@class="header__top-description"]').click()

    with allure.step('Выбираем окно ввода и набираем г Новосибирск'):
        search_input = driver.find_element_by_xpath('//input[@class="text-field text-field_large"]').send_keys(
            "г Новосибирск")
        city = 'г Новосибирск'

    with allure.step('Выбираем г Новосибирск из списка саджестов'):
        suggests = driver.find_elements_by_xpath('//ul[@class="geo__suggest"]//li[@class="suggest__item"]')

        for suggest in suggests:
            if suggest.find_element_by_xpath('//span[@class="suggest__item-query"]').text == city:
                suggest.click()
            break
        else:
            raise Exception(f'Среди подсказок отсутствует {city_name}')

    with allure.step('Нажимаем подтвержить выбор'):
        search_button = driver.find_element_by_xpath('//button[@class="button button_blue geo__button-save"]').click()

    with allure.step('Перезагружаем страницу'):
        driver.refresh()

    with allure.step('Проверяем что выбор города сохранился после перезагрузки страницы'):
        search_current_city = driver.find_element_by_xpath(
            '*//span[@class="header__top-description-region-name arrow-bottom arrow-bottom_geo"][contains( text(),"г Новосибирск")]')
        assert search_current_city.text == "г Новосибирск"
