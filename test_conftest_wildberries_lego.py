from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


@allure.title('Проверяем добавление товаров Лего в корзину')
@allure.severity(Severity.NORMAL)
def test_conftest_lego(driver: WebDriver):
    driver.implicitly_wait(10)
    with allure.step('Открываем главную страницу Вайдберриз'):
        driver.get('https://www.wildberries.ru/')

    with allure.step('Ищем и выбираем баннер с распродажей Lego'):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="part-2"]/div[1]/div[2]/div[1]/div/div/a'))
            )
            element.click()
        except TimeoutError:
            print('Not found')

    with allure.step('Выбираем товары на складе в Москве'):
        try:
            driver.execute_script("window.scrollTo(0, 950)")
            box = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="filterblock store show"]'))
            )
            box.click()
            driver.find_element_by_xpath('//a[text()="Москва"]').click()
        except TimeoutError:
            print('Not found')

    with allure.step('Выбирает фильтр по цене и ставим до 1000 рублей'):
        try:
            driver.execute_script("window.scrollTo(0, 450)")
            price = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="filterblock price show"]'))
            )
            price.click()
        except TimeoutError:
            print('Not found')

        driver.execute_script("window.scrollTo(0, 750)")
        price_filed = driver.find_element_by_xpath('//input[@name="endN"]')
        price_filed.send_keys("1000")
        price_filed.send_keys(Keys.ENTER)

    with allure.step('Ищем фигурку Рей из Звездных войн'):
        driver.find_element_by_xpath('//div[@id="c4503733"]').click()