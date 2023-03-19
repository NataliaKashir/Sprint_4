import allure
import time
from locators.add_order_locator.form_for_whom_locator import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class FormPageForWhomScooter:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки формы Для кого самокат')
    def wait_for_load_add_order_for_whom_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(order_phone))

    @allure.step('Заполнение формы Для кого самокат')
    def fill_order_scooter_for_whom_form(self, name, surname, address, metro, text_metro, phone):
        self.driver.find_element(*order_name).send_keys(name)
        self.driver.find_element(*order_surname).send_keys(surname)
        self.driver.find_element(*order_address).send_keys(address)
        self.driver.find_element(*order_phone).send_keys(phone)
        self.driver.find_element(*order_metro).click
        # без данных действий иногда не отрабатывает скрипт по выпадающему списку по причине долгой загрузки странички (у меня)
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
