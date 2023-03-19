import allure
from pages.main_page import *
from pages.base_page import *

class TestMainPageQuestionsScooter:
    # вопрос Сколько это стоит? И как оплатить?
    question_0_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    # вопрос Хочу сразу несколько самокатов! Так можно?
    question_1_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    # вопрос Как рассчитывается время аренды?
    question_2_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    # вопрос Можно ли заказать самокат прямо на сегодня?
    question_3_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    # вопрос Можно ли продлить заказ или вернуть самокат раньше?
    question_4_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    # вопрос Вы привозите зарядку вместе с самокатом?
    question_5_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    # вопрос Можно ли отменить заказ?
    question_6_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    # вопрос Я жизу за МКАДом, привезёте?
    question_7_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    @allure.title('Проверка при нажатии на вопрос 0 - открывается соответствующий текст')
    @allure.description('На странице кликаем на вопрос 0, проверяем, что его текст соответсвует ожиданиям и элемент ответа не hidden')
    def test_check_question_0(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.scroll_to_questions()
        main_page.wait_for_scroll_main_page()
        main_page.click_question_0_div()
        question_0_text_result = main_page.get_question_0_text()
        hidden = main_page.get_answer_0_div().get_attribute('hidden')
        assert hidden == None, f'Ожидалось что элемент с ответом 0 будет НЕ скрыт: None, получено "{hidden}"'
        assert question_0_text_result == self.question_0_text, f'Ожидалось значение ответа на вопрос 0: "{self.question_0_text}", получено "{question_0_text_result}"'

    @allure.title('Проверка при нажатии на вопрос 1 - открывается соответствующий текст')
    @allure.description('На странице кликаем на вопрос 1, проверяем, что его текст соответсвует ожиданиям и элемент ответа не hidden')
    def test_check_question_1(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.scroll_to_questions()
        main_page.wait_for_scroll_main_page()
        main_page.click_question_1_div()
        question_1_text_result = main_page.get_question_1_text()
        hidden = main_page.get_answer_1_div().get_attribute('hidden')
        assert hidden == None, f'Ожидалось что элемент с ответом 1 будет НЕ скрыт: None, получено "{hidden}"'
        assert question_1_text_result == self.question_1_text, f'Ожидалось значение ответа на вопрос 1: "{self.question_1_text}", получено "{question_1_text_result}"'

    @allure.title('Проверка при нажатии на вопрос 2 - открывается соответствующий текст')
    @allure.description('На странице кликаем на вопрос 2, проверяем, что его текст соответсвует ожиданиям и элемент ответа не hidden')
    def test_check_question_2(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.scroll_to_questions()
        main_page.wait_for_scroll_main_page()
        main_page.click_question_2_div()
        question_2_text_result = main_page.get_question_2_text()
        hidden = main_page.get_answer_2_div().get_attribute('hidden')
        assert hidden == None, f'Ожидалось что элемент с ответом 2 будет НЕ скрыт: None, получено "{hidden}"'
        assert question_2_text_result == self.question_2_text, f'Ожидалось значение ответа на вопрос 2: "{self.question_2_text}", получено "{question_2_text_result}"'

    @allure.title('Проверка при нажатии на вопрос 3 - открывается соответствующий текст')
    @allure.description('На странице кликаем на вопрос 3, проверяем, что его текст соответсвует ожиданиям и элемент ответа не hidden')
    def test_check_question_3(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.scroll_to_questions()
        main_page.wait_for_scroll_main_page()
        main_page.click_question_3_div()
        question_3_text_result = main_page.get_question_3_text()
        hidden = main_page.get_answer_3_div().get_attribute('hidden')
        assert hidden == None, f'Ожидалось что элемент с ответом 3 будет НЕ скрыт: None, получено "{hidden}"'
        assert question_3_text_result == self.question_3_text, f'Ожидалось значение ответа на вопрос 3: "{self.question_3_text}", получено "{question_3_text_result}"'

    @allure.title('Проверка при нажатии на вопрос 4 - открывается соответствующий текст')
    @allure.description('На странице кликаем на вопрос 4, проверяем, что его текст соответсвует ожиданиям и элемент ответа не hidden')
    def test_check_question_4(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.scroll_to_questions()
        main_page.wait_for_scroll_main_page()
        main_page.click_question_4_div()
        question_4_text_result = main_page.get_question_4_text()
        hidden = main_page.get_answer_4_div().get_attribute('hidden')
        assert hidden == None, f'Ожидалось что элемент с ответом 4 будет НЕ скрыт: None, получено "{hidden}"'
        assert question_4_text_result == self.question_4_text, f'Ожидалось значение ответа на вопрос 4: "{self.question_4_text}", получено "{question_4_text_result}"'

    @allure.title('Проверка при нажатии на вопрос 5 - открывается соответствующий текст')
    @allure.description('На странице кликаем на вопрос 5, проверяем, что его текст соответсвует ожиданиям и элемент ответа не hidden')
    def test_check_question_5(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.scroll_to_questions()
        main_page.wait_for_scroll_main_page()
        main_page.click_question_5_div()
        question_5_text_result = main_page.get_question_5_text()
        hidden = main_page.get_answer_5_div().get_attribute('hidden')
        assert hidden == None, f'Ожидалось что элемент с ответом 5 будет НЕ скрыт: None, получено "{hidden}"'
        assert question_5_text_result == self.question_5_text, f'Ожидалось значение ответа на вопрос 5: "{self.question_5_text}", получено "{question_5_text_result}"'

    @allure.title('Проверка при нажатии на вопрос 6 - открывается соответствующий текст')
    @allure.description('На странице кликаем на вопрос 6, проверяем, что его текст соответсвует ожиданиям и элемент ответа не hidden')
    def test_check_question_6(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.scroll_to_questions()
        main_page.wait_for_scroll_main_page()
        main_page.click_question_6_div()
        question_6_text_result = main_page.get_question_6_text()
        hidden = main_page.get_answer_6_div().get_attribute('hidden')
        assert hidden == None, f'Ожидалось что элемент с ответом 6 будет НЕ скрыт: None, получено "{hidden}"'
        assert question_6_text_result == self.question_6_text, f'Ожидалось значение ответа на вопрос 6: "{self.question_6_text}", получено "{question_6_text_result}"'

    @allure.title('Проверка при нажатии на вопрос 7 - открывается соответствующий текст')
    @allure.description('На странице кликаем на вопрос 7, проверяем, что его текст соответсвует ожиданиям и элемент ответа не hidden')
    def test_check_question_7(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.scroll_to_questions()
        main_page.wait_for_scroll_main_page()
        main_page.click_question_7_div()
        question_7_text_result = main_page.get_question_7_text()
        hidden = main_page.get_answer_7_div().get_attribute('hidden')
        assert hidden == None, f'Ожидалось что элемент с ответом 7 будет НЕ скрыт: None, получено "{hidden}"'
        assert question_7_text_result == self.question_7_text, f'Ожидалось значение ответа на вопрос 7: "{self.question_7_text}", получено "{question_7_text_result}"'