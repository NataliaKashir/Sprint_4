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
        for_whom.check_input_data_for_whom_form(OD.name, OD.surname, OD.address, OD.text_metro, OD.phone)

        about_rent = FormPageAboutRentScooter(driver)
        for_whom.click_order_scooter_for_whom_form_next_btn()
        about_rent.wait_for_load_element(order_btn)
        about_rent.fill_order_scooter_about_rent_form(OD.text_date, OD.days, OD.color, OD.comment)
        about_rent.check_input_data_about_rent_form(OD.text_date, OD.color_input, OD.comment, OD.text_days)

        about_rent.click_about_rent_form_order_btn()
        about_rent.wait_for_load_element(order_btn_confirm)
        about_rent.click_order_btn_confirm()
        actually_ordered_header = about_rent.get_ordered_popup_window_header()
        assert "Заказ оформлен" in actually_ordered_header, f'Ожидалось что окно подтверждения создания заказа будет содержать "Заказ оформлен", получено {actually_ordered_header}'
