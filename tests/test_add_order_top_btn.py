import pytest
import allure
from pages.add_order_pages.form_for_whom import *
from pages.add_order_pages.form_about_rent import *
from pages.base_page import *
from test_data import *

class TestAddOrderTopBtnScooter:

    @allure.title('Проверка заказа самоката при нажатии на верхнюю кнопку Заказать главной страницы')
    @allure.description('Заполняем формы оформления заказа для позитивного сценария')
    @pytest.mark.parametrize('order_test_data', order_test_data_list)
    def test_add_order_top_btn(self, driver, order_test_data):
        base_page = BasePageScooter(driver)
        for_whom = FormPageForWhomScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        base_page.click_top_order_btn()
        # переменные тестового набора данных заказа
        name = order_test_data['name']
        surname = order_test_data['surname']
        address = order_test_data['address']
        metro = order_test_data['metro']
        text_metro = order_test_data['text_metro']
        phone = order_test_data['phone']
        text_date = order_test_data['text_date']
        days = order_test_data['days']
        text_days = order_test_data['text_days']
        color = order_test_data['color']
        color_input = order_test_data['color_input']
        comment = order_test_data['comment']

        for_whom.fill_order_scooter_for_whom_form(name, surname, address, metro, text_metro, phone)

        actually_name_value = for_whom.get_for_whom_form_name()
        actually_surname_value = for_whom.get_for_whom_form_surname()
        actually_address_value = for_whom.get_for_whom_form_address()
        actually_metro_value = for_whom.get_for_whom_form_metro()
        actually_phone_value = for_whom.get_for_whom_form_phone()
        # проверяем корректность заполнения полей
        assert actually_name_value == name, f'Ожидалось что поле Имя будет содержать {name}, получено {actually_name_value}'
        assert actually_surname_value == surname, f'Ожидалось что поле Фамилия будет содержать {surname}, получено {actually_surname_value}'
        assert actually_address_value == address, f'Ожидалось что поле Адрес будет содержать {address}, получено {actually_address_value}'
        assert actually_metro_value == text_metro, f'Ожидалось что поле Метро будет содержать {text_metro}, получено {actually_metro_value}'
        assert actually_phone_value == phone, f'Ожидалось что поле Телефон будет содержать {phone}, получено {actually_phone_value}'

        for_whom = FormPageForWhomScooter(driver)
        about_rent = FormPageAboutRentScooter(driver)
        for_whom.click_order_scooter_for_whom_form_next_btn()
        about_rent.wait_for_load_add_order_about_rent_page()
        about_rent.fill_order_scooter_about_rent_form(text_date, days, color, comment)

        actually_date_value = about_rent.get_about_rent_form_date()
        actually_days_value = about_rent.get_about_rent_form_days()
        actually_color_value = about_rent.get_about_rent_form_color(color_input)
        actually_comment_value = about_rent.get_about_rent_form_comment()
        # проверяем корректность заполнения полей
        assert actually_date_value == text_date, f'Ожидалось что поле Дата будет содержать {text_date}, получено {actually_date_value}'
        assert actually_days_value == text_days, f'Ожидалось что поле Срок аренды будет содержать {text_days}, получено {actually_days_value}'
        assert actually_color_value == True, f'Ожидалось что проверка Цвета будет True, получено {actually_color_value}'
        assert actually_comment_value == comment, f'Ожидалось что поле Комментарий будет содержать {comment}, получено {actually_comment_value}'

        # нажимаем кнопку Заказать формы Про аренду
        about_rent.click_about_rent_form_order_btn()
        about_rent.wait_confirmation_order_window()
        about_rent.click_order_btn_confirm()
        actually_ordered_header = about_rent.get_ordered_popup_window_header()
        assert "Заказ оформлен" in actually_ordered_header, f'Ожидалось что окно подтверждения создания заказа будет содержать "Заказ оформлен", получено {actually_ordered_header}'
