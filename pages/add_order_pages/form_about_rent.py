import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_data import *
from pages.base_page import *

class FormPageAboutRentScooter(BasePageScooter):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполняем форму Про аренду')
    def fill_order_scooter_about_rent_form(self, text_date, days, color, comment):
        self.driver.find_element(*order_date).send_keys(text_date)
        self.driver.find_element(*header_about_rent).click()
        self.driver.find_element(*order_days).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(days))
        self.driver.find_element(*days).click()
        self.driver.find_element(*color).click()
        self.driver.find_element(*order_comment).send_keys(comment)

    @allure.step('Нажимаем кнопку Далее на форме Про аренду')
    def click_order_scooter_about_rent_form_next_btn(self):
        self.driver.find_element(*order_btn).click()

    @allure.step('Получаем установленное значение поля Когда привезти самокат')
    def get_about_rent_form_date(self):
        return self.driver.find_element(*order_date).get_property("value")

    @allure.step('Получаем установленное значение поля Срок аренды')
    def get_about_rent_form_days(self):
        return self.driver.find_element(*order_days_selected).text

    @allure.step('Получаем установленное значение поля Цвет')
    def get_about_rent_form_color(self, color_input):
        return self.driver.find_element(*color_input).get_property("checked")

    @allure.step('Получаем установленное значение поля Когмментарий')
    def get_about_rent_form_comment(self):
        return self.driver.find_element(*order_comment).get_property("value")

    @allure.step('Нажимаем кнопку Заказать в форме Про аренду')
    def click_about_rent_form_order_btn(self):
        return self.driver.find_element(*order_btn).click()

    @allure.step('Нажимаем кнопку подтверждения заказа')
    def click_order_btn_confirm(self):
        return self.driver.find_element(*order_btn_confirm).click()

    @allure.step('Получаем текст заголовка всплывающего окна заказа')
    def get_ordered_popup_window_header(self):
        return self.driver.find_element(*ordered_header).text

    @allure.step('Проверяем, что данные в форму Про аренду введены корректно')
    def check_input_data_about_rent_form(self, text_date, color_input, comment, text_days):
        assert self.get_about_rent_form_date() == text_date, f'Ожидалось что поле Дата будет содержать {text_date}, получено {self.get_about_rent_form_date()}'
        assert self.get_about_rent_form_days() == text_days, f'Ожидалось что поле Срок аренды будет содержать {text_days}, получено {self.get_about_rent_form_days()}'
        assert self.get_about_rent_form_color(color_input) == True, f'Ожидалось что проверка Цвета будет True, получено {self.get_about_rent_form_color(color_input)}'
        assert self.get_about_rent_form_comment() == comment, f'Ожидалось что поле Комментарий будет содержать {comment}, получено {self.get_about_rent_form_comment()}'
