from builtins import list, ConnectionAbortedError, Exception

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

@allure.title('Проверяем смену города в разделе о доставке')
def test_lamoda_delivery():
    driver = WebDriver(executable_path='C://python//chromedriver.exe')
    driver.implicitly_wait(10)
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

    with allure.step('Переходим на страницу Условия Доставки'):
        search_button = driver.find_element_by_xpath('//a[@class="link footer__link"][contains( text(), "Условия доставки")]').click()

    with allure.step('Меняем город доставки на Москву'):
        search_input = driver.find_element_by_xpath('//input[@class="text-field js-suggested-input"]').clear()
        search_input = driver.find_element_by_xpath('//input[@class="text-field js-suggested-input"]').send_keys('г Москва')

    with allure.step('Из списка саджестов выбираем Москву и подтверждаем выбор'):
        suggest = driver.find_element_by_xpath('//span[@class="suggest__item-query"]').click()

    with allure.step('Проверяем кол-во вариантов доставки, сроки и стоимость'):
        CountOfXpath = driver.find_elements_by_xpath('//div[@class="delivery_item-name_type"]')
        for Count in CountOfXpath:
            if driver.find_elements_by_xpath('//div[@class="delivery_item-name_type"]').__len__() == 5:
                break
            else:
                raise Exception(f'Вариантов доставки больше чем 5')





