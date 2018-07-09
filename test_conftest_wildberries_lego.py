from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

@allure.title('Проверяем добавление товаров Лего в корзину')
@allure.severity(Severity.NORMAL)
def test_conftest_lego(driver: WebDriver):
    driver.implicitly_wait(5)
    with allure.step('Открываем главную страницу Вайдберриз'):
        driver.get('https://www.wildberries.ru/')

    with allure.step('Ищем и выбираем баннер с распродажей Lego'):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="part-2"]/div[1]/div[2]/div[1]/div/div/a'))
            )
            element.click()
        except Exception:
            print('Not found')

    with allure.step('Выбираем товары на складе в Москве'):
        try:
            box = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="filterPanelLeft"]/div[3]/div[1]/text()'))
            )
            box.click()
            driver.find_element_by_xpath('//*[@id="store_list_left"]/li[1]/a/i').click()
        except Exception:
            print('Not found')

    with allure.step('Выбирает фильтр по цене и ставим до 1000 рублей'):
        driver.find_element_by_xpath('//*[@id="filterPanelLeft"]/div[4]/div[1]/text()').click()
        driver.find_element(By.NAME, 'endN').clear()
        driver.find_element(By.NAME, 'endN').send_keys(1000)