import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options
from locators.main_page_locators import MainPageLocators

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=options)
    driver.get(BASE_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def close_cookie(driver):
    # Закрываем окно с куки, если кнопка отображается и кликабельна
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPageLocators.CONFIRM_COOKIE_BUTTON)).click()