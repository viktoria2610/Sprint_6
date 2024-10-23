import allure
from pages.base_page import BasePage
from locators.transition_page_locators import TransitionPageLocators
from locators.header_page_locators import HeaderPageLocators

class TransitionPage(BasePage):

    @allure.step('Проверяем, что при клике по логотипу Самоката осуществляется переход на главную страницу')
    def check_scooter_logo_transition(self):
        self.click_to_element(HeaderPageLocators.HEADER_ORDER_BUTTON)
        self.click_to_element(HeaderPageLocators.SCOOTER_LOGO)
        return self.get_text_from_element(TransitionPageLocators.MAIN_TITLE)

    @allure.step('Проверяем, что при клике по логотипу Яндекса осуществляется переход на Яндекс Дзен')
    def check_yandex_logo_transition(self):
        self.click_to_element(HeaderPageLocators.YANDEX_LOGO)
        self.switch_to_last_tab()
        self.find_element_with_wait(TransitionPageLocators.DZEN_LOCATORS)