import allure
from pages.transition_page import TransitionPage

class TestTransition:
    @allure.title('Переход по логотипу Самоката')
    @allure.description('Проверяем, что осуществляется переход по клику по логотипу Самоката')
    def test_scooter_logo_transition(self, driver, close_cookie):
        main_title_text = "Самокат\nна пару дней"
        transition_page = TransitionPage(driver)
        assert main_title_text in transition_page.check_scooter_logo_transition()
    @allure.title('Переход по логотипу Яндекса')
    @allure.description('Проверяем, что осуществляется переход по клику по логотипу Яндекса')
    def test_yandex_logo_transition(self, driver, close_cookie):
        yandex_logo_text = 'Логотип Бренда'
        transition_page = TransitionPage(driver)
        assert yandex_logo_text in transition_page.check_yandex_logo_transition()