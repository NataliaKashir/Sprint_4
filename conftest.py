import pytest
import allure
from selenium import webdriver


@allure.title('Открываем/Закрываем браузер')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver

    driver.quit()