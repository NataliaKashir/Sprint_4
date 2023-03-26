import allure
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_data import *

class FormPageAboutRentScooter:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем загрузку страницы Про аренду')
    def wait_for_load_add_order_about_rent_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(order_btn))
    @allure.step('Ожидаем появление окна страницы Хотите оформить заказ?')
    def wait_confirmation_order_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(order_btn_confirm))

    @allure.step('Заполняем форму Про аренду')
    def fill_order_scooter_about_rent_form(self, text_date, days, color, comment):
        self.driver.find_element(*order_date).send_keys(text_date)
        self.driver.find_element(*header_about_rent).click()
        self.driver.find_element(*order_days).click()
        # ждем выпадающего списка дней аренды
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
