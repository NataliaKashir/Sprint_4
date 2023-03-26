from locators.add_order_locator.form_about_rent_locator import *
from locators.add_order_locator.form_for_whom_locator import *

class OrderData1:
    name = "Иван"
    surname = "Иванов"
    address = "Тверская улица, 28"
    metro = order_metro_dropdown1
    text_metro = "Маяковская"
    phone = "+79877777777"
    text_date = "02.04.2023"
    days = order_days_dropdown1
    text_days = "четверо суток"
    color = order_color_black
    color_input = order_color_black_input
    comment = "Тестовый комментарий 1"

class OrderData2:
    name = "Петр"
    surname = "Петров"
    address = "Тверская улица, 82"
    metro = order_metro_dropdown2
    text_metro = "Красносельская"
    phone = "+7988888888"
    text_date = "01.04.2023"
    days = order_days_dropdown2
    text_days = "семеро суток"
    color = order_color_grey
    color_input = order_color_grey_input
    comment = "Тестовый комментарий 2"

order_test_data_list = [ OrderData1, OrderData2 ]