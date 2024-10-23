import allure
import pytest

from pages.order_page import OrderPage
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators

class TestOrderPage:
    @pytest.mark.parametrize(
        'name, last_name, address, phone, comment, order_button',
        [
            ('Иван', 'Иванов', 'Москва, ул.Кирова, д.36', '89119998877', 'Тест первого заказа', HeaderPageLocators.HEADER_ORDER_BUTTON),
            ('Петр', 'Петров', 'Санкт-Петербург, ул.Ленина, д.12', '+79998887766', 'Тест второго заказа', MainPageLocators.MAIN_ORDER_BUTTON)
        ]
    )
    @allure.title('Создание заказа')
    @allure.description('Проверяем, что заказ успешно создан')
    def test_success_order(self, driver, close_cookie, name, last_name, address, phone, comment, order_button):
        expected_text = "Заказ оформлен"
        order_page = OrderPage(driver)
        order_page.set_order(name,last_name,address,phone,comment, order_button)
        assert expected_text in order_page.check_order()
