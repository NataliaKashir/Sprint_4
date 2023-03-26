import pytest
import time
import allure
from pages.add_order_pages.form_for_whom import *
from pages.add_order_pages.form_about_rent import *
from pages.base_page import *
from pages.main_page import *
from test_data import *

class TestAddOrderBottomBtnScooter:

    @allure.title('Проверка заказа самоката при нажатии на нижнюю кнопку Заказать главной страницы')
    @allure.description('Заполняем формы оформления заказа для позитивного сценария')
    @pytest.mark.parametrize('OD', order_test_data_list)
    def test_add_order_bottom_btn(self, driver, OD):
        base_page = BasePageScooter(driver)
        main_page = MainPageScooter(driver)
        for_whom = FormPageForWhomScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        base_page.scroll_to_bottom_order_btn()
        base_page.wait_for_visibility_bottom_order_btn()
        main_page.click_bottom_order_btn()

        for_whom.fill_order_scooter_for_whom_form(OD.name, OD.surname, OD.address, OD.metro, OD.text_metro, OD.phone)

        actually_name_value = for_whom.get_for_whom_form_name()
        actually_surname_value = for_whom.get_for_whom_form_surname()
        actually_address_value = for_whom.get_for_whom_form_address()
        actually_metro_value = for_whom.get_for_whom_form_metro()
        actually_phone_value = for_whom.get_for_whom_form_phone()
        assert actually_name_value == OD.name, f'Ожидалось что поле Имя будет содержать {OD.name}, получено {actually_name_value}'
        assert actually_surname_value == OD.surname, f'Ожидалось что поле Фамилия будет содержать {OD.surname}, получено {actually_surname_value}'
        assert actually_address_value == OD.address, f'Ожидалось что поле Адрес будет содержать {OD.address}, получено {actually_address_value}'
        assert actually_metro_value == OD.text_metro, f'Ожидалось что поле Метро будет содержать {OD.text_metro}, получено {actually_metro_value}'
        assert actually_phone_value == OD.phone, f'Ожидалось что поле Телефон будет содержать {OD.phone}, получено {actually_phone_value}'

        for_whom = FormPageForWhomScooter(driver)
        about_rent = FormPageAboutRentScooter(driver)
        for_whom.click_order_scooter_for_whom_form_next_btn()
        about_rent.wait_for_load_element(order_btn)
        about_rent.fill_order_scooter_about_rent_form(OD.text_date, OD.days, OD.color, OD.comment)

        actually_date_value = about_rent.get_about_rent_form_date()
        actually_days_value = about_rent.get_about_rent_form_days()
        actually_color_value = about_rent.get_about_rent_form_color(OD.color_input)
        actually_comment_value = about_rent.get_about_rent_form_comment()
        assert actually_date_value == OD.text_date, f'Ожидалось что поле Дата будет содержать {OD.text_date}, получено {actually_date_value}'
        assert actually_days_value == OD.text_days, f'Ожидалось что поле Срок аренды будет содержать {OD.text_days}, получено {actually_days_value}'
        assert actually_color_value == True, f'Ожидалось что проверка Цвета будет True, получено {actually_color_value}'
        assert actually_comment_value == OD.comment, f'Ожидалось что поле Комментарий будет содержать {OD.comment}, получено {actually_comment_value}'

        about_rent.click_about_rent_form_order_btn()
        about_rent.wait_for_load_element(order_btn_confirm)
        about_rent.click_order_btn_confirm()
        actually_ordered_header = about_rent.get_ordered_popup_window_header()
        assert "Заказ оформлен" in actually_ordered_header, f'Ожидалось что окно подтверждения создания заказа будет содержать "Заказ оформлен", получено {actually_ordered_header}'
