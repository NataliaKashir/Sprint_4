import allure
import time
from pages.main_page import *
from pages.base_page import *

class TestMainPageLinksScooter:

    @allure.title('Проверка при нажатии на надпись Самокат в логотипе - открывается главная страница Самоката')
    @allure.description('На главной странице кликаем на кнопку Заказать, потом на Самокат в логотипе, проверяем, что находимся на гланой странице Самоката')
    def test_check_logo_scooter(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.click_top_order_btn()
        current_url = driver.current_url
        assert current_url == order_page_url, f'Ожидалось что текущий url будет {order_page_url}, получено "{current_url}"'
        main_page.click_logo_scooter()
        current_url = driver.current_url
        assert current_url == main_page_url, f'Ожидалось что текущий url будет {main_page_url}, получено "{current_url}"'

    @allure.title('Проверка при нажатии на надпись Яндекс в логотипе - открывается главная страница Яндекса')
    @allure.description('На главной странице кликаем на надпись Яндекс в логотипе, проверяем, что находимся на главной странице Яндекса')
    def test_check_logo_yandex(self, driver):
        main_page = MainPageScooter(driver)
        base_page = BasePageScooter(driver)
        base_page.open_main_page()
        base_page.wait_for_load_main_page()
        main_page.click_logo_yandex()
        WebDriverWait(driver, 3).until(expected_conditions.number_of_windows_to_be(2))
        # ждем прогрузки яндекса после всех редиректов (так долго потому что проблема с сетью на моей стороне)
        time.sleep(10)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        current_url = driver.current_url
        assert current_url == yandex_main_page_url, f'Ожидалось что текущий url будет {yandex_main_page_url}, получено "{current_url}"'



