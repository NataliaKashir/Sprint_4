import allure
import time
from locators.add_order_locator.form_for_whom_locator import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import *

class FormPageForWhomScooter(BasePageScooter):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение формы Для кого самокат')
    def fill_order_scooter_for_whom_form(self, name, surname, address, metro, text_metro, phone):
        self.driver.find_element(*order_name).send_keys(name)
        self.driver.find_element(*order_surname).send_keys(surname)
        self.driver.find_element(*order_address).send_keys(address)
        self.driver.find_element(*order_phone).send_keys(phone)
        self.driver.find_element(*order_metro).click
        # не убираю ожидание, но просто send_keys в метро не работают, пока не выберешь элемент.
        # Вынуждена оставить выбор элемента и ожидание, т.к., может быть, причина в моей проблеме с сетью.
        time.sleep(1)
        self.driver.find_element(*order_metro).send_keys(text_metro)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(metro))
        self.driver.find_element(*metro).click()

    @allure.step('Клик по кнопке Далее формы Для кого самокат')
    def click_order_scooter_for_whom_form_next_btn(self):
        self.driver.find_element(*form_for_whom_next_btn).click()

    @allure.step('Получаем установленное значение поля Имя')
    def get_for_whom_form_name(self):
        return self.driver.find_element(*order_name).get_property("value")

    @allure.step('Получаем установленное значение поля Фамилия')
    def get_for_whom_form_surname(self):
        return self.driver.find_element(*order_surname).get_property("value")

    @allure.step('Получаем установленное значение поля Адрес')
    def get_for_whom_form_address(self):
        return self.driver.find_element(*order_address).get_property("value")

    @allure.step('Получаем установленное значение поля Метро')
    def get_for_whom_form_metro(self):
        return self.driver.find_element(*order_metro).get_property("value")

    @allure.step('Получаем установленное значение поля Телефон')
    def get_for_whom_form_phone(self):
        return self.driver.find_element(*order_phone).get_property("value")

    @allure.step('Проверяем, что данные в форму Для кого самокат введены корректно')
    def check_input_data_for_whom_form(self, name, surname, address, text_metro, phone):
        actually_name_value = self.get_for_whom_form_name()
        actually_surname_value = self.get_for_whom_form_surname()
        actually_address_value = self.get_for_whom_form_address()
        actually_metro_value = self.get_for_whom_form_metro()
        actually_phone_value = self.get_for_whom_form_phone()
        assert actually_name_value == name, f'Ожидалось что поле Имя будет содержать {name}, получено {actually_name_value}'
        assert actually_surname_value == surname, f'Ожидалось что поле Фамилия будет содержать {surname}, получено {actually_surname_value}'
        assert actually_address_value == address, f'Ожидалось что поле Адрес будет содержать {address}, получено {actually_address_value}'
        assert actually_metro_value == text_metro, f'Ожидалось что поле Метро будет содержать {text_metro}, получено {actually_metro_value}'
        assert actually_phone_value == phone, f'Ожидалось что поле Телефон будет содержать {phone}, получено {actually_phone_value}'

