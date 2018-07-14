from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import allure

@allure.title('Ищем станицу википедии о Милонове')
@allure.severity(Severity.BLOCKER)
def test_yandex_search():
    driver = WebDriver(executable_path='D://allure//chromedriver.exe')
    with allure.step('Открываем страницу яндекса'):
        driver.get('https://ya.ru')

    with allure.step('Ищем Виталия Милонова'):
        search_input = driver.find_element_by_xpath('//input[@id="text"]')
        search_button = driver.find_element_by_xpath('//div[@class="search2__button"]//button[@type="submit"]')
        search_input.send_keys('Виталий Милонов')
        search_button.click()

    def check_results_count(driver):
        search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(search_results) >= 10
    with allure.step('Ожидаем, что количество результатов теста больше 10'):
        WebDriverWait(driver, 5, 0.5).until(check_results_count, 'Количество результатов поиска меньше 10')

    with allure.step('Переходим по ссылке первого результата'):
        search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        link = search_results[0].find_element_by_xpath('.//h2/a')
        link.click()

    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Проверяем корректность Title страницы'):
        assert driver.title == 'Милонов, Виталий Валентинович — Википедия'
