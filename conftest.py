import pytest
import allure
from selenium import webdriver


@allure.step('Открываем браузер')
@allure.step('Закрываем браузер')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver

    driver.quit()