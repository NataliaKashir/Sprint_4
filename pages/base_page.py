import allure
from locators.main_page_locator import MainPageBottomElements as MPB
from locators.main_page_locator import MainPageQuestionsElements as MPQ
from urls import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.driver.get(main_page_url)

    @allure.step('Ожидаем загрузку главной страницы')
    def wait_for_load_main_page(self):
        # ставлю ожидание 10, потому что Яндекс Самокат открывается оооочень долго в Firefix (у меня)
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(MPQ.question_7))

    @allure.step('Скролл до нижней кнопки Заказать')
    def scroll_to_bottom_order_btn(self):
        bottom_btn = self.driver.find_element(*MPB.order_scooter_bottom_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", bottom_btn)

    @allure.step('Ожидание отображения нижней кнопки Заказать')
    def wait_for_visibility_bottom_order_btn(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MPB.order_scooter_bottom_btn))

    @allure.step('Ожидаем загрузку элемента {element}')
    def wait_for_load_element(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(element))
