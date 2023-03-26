import allure
from locators.main_page_locator import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MainPageScooter:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание отображения последнего элемента вопроса на главной странице')
    def wait_for_scroll_main_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(question_7))

    @allure.step('Скрол до последнего элемента вопроса на главной странице')
    def scroll_to_questions(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*question_7))

    @allure.step('Клик по вопросу 0')
    def click_question_0_div(self):
        self.driver.find_element(*question_0).click()

    @allure.step('Клик по вопросу 1')
    def click_question_1_div(self):
        self.driver.find_element(*question_1).click()

    @allure.step('Клик по вопросу 2')
    def click_question_2_div(self):
        self.driver.find_element(*question_2).click()

    @allure.step('Клик по вопросу 3')
    def click_question_3_div(self):
        self.driver.find_element(*question_3).click()

    @allure.step('Клик по вопросу 4')
    def click_question_4_div(self):
        self.driver.find_element(*question_4).click()

    @allure.step('Клик по вопросу 5')
    def click_question_5_div(self):
        self.driver.find_element(*question_5).click()

    @allure.step('Клик по вопросу 6')
    def click_question_6_div(self):
        self.driver.find_element(*question_6).click()

    @allure.step('Клик по вопросу 7')
    def click_question_7_div(self):
        self.driver.find_element(*question_7).click()

    @allure.step('Получаем текст к по вопросу 0')
    def get_question_0_text(self):
        return self.driver.find_element(*answer_0_p).text

    @allure.step('Получаем текст к по вопросу 1')
    def get_question_1_text(self):
        return self.driver.find_element(*answer_1_p).text

    @allure.step('Получаем текст к по вопросу 2')
    def get_question_2_text(self):
        return self.driver.find_element(*answer_2_p).text

    @allure.step('Получаем текст к по вопросу 3')
    def get_question_3_text(self):
        return self.driver.find_element(*answer_3_p).text

    @allure.step('Получаем текст к по вопросу 4')
    def get_question_4_text(self):
        return self.driver.find_element(*answer_4_p).text

    @allure.step('Получаем текст к по вопросу 5')
    def get_question_5_text(self):
        return self.driver.find_element(*answer_5_p).text

    @allure.step('Получаем текст к по вопросу 6')
    def get_question_6_text(self):
        return self.driver.find_element(*answer_6_p).text

    @allure.step('Получаем текст к по вопросу 7')
    def get_question_7_text(self):
        return self.driver.find_element(*answer_7_p).text

    @allure.step('Получаем элемент ответа 0')
    def get_answer_0_div(self):
        return self.driver.find_element(*answer_0_div)

    @allure.step('Получаем элемент ответа 1')
    def get_answer_1_div(self):
        return self.driver.find_element(*answer_1_div)

    @allure.step('Получаем элемент ответа 2')
    def get_answer_2_div(self):
        return self.driver.find_element(*answer_2_div)

    @allure.step('Получаем элемент ответа 3')
    def get_answer_3_div(self):
        return self.driver.find_element(*answer_3_div)

    @allure.step('Получаем элемент ответа 4')
    def get_answer_4_div(self):
        return self.driver.find_element(*answer_4_div)

    @allure.step('Получаем элемент ответа 5')
    def get_answer_5_div(self):
        return self.driver.find_element(*answer_5_div)

    @allure.step('Получаем элемент ответа 6')
    def get_answer_6_div(self):
        return self.driver.find_element(*answer_6_div)

    @allure.step('Получаем элемент ответа 7')
    def get_answer_7_div(self):
        return self.driver.find_element(*answer_7_div)

    @allure.step('Клик по надписи Самокат в логотипе')
    def click_logo_scooter(self):
        self.driver.find_element(*logo_scooter).click()

    @allure.step('Клик по надписи Яндекс в логотипе')
    def click_logo_yandex(self):
        self.driver.find_element(*logo_yandex).click()
