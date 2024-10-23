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
    yield driver
    driver.quit()

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.confirm_cookie_button = MainPageLocators.CONFIRM_COOKIE_BUTTON

    def click_confirm_cookie_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.confirm_cookie_button)).click()

@pytest.fixture(scope="function")
def close_cookie(driver):
    main_page = MainPage(driver)
    main_page.click_confirm_cookie_button()
