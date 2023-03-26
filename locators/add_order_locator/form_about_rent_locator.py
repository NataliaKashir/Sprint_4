from selenium.webdriver.common.by import By

# форма Про аренду

# поле Когда привезти самокат
order_date = [By.XPATH, '//*[@placeholder="* Когда привезти самокат"]']
# Заголовок Про аренду
header_about_rent = [By.XPATH, "//*[starts-with(text(),'Про аренду')]"]
# поле Срок аренды
order_days = [By.XPATH, "//*[starts-with(text(),'* Срок аренды')]"]
# поле Срок аренды выпадающий список
order_days_dropdown1 = [By.XPATH, "//*[starts-with(text(),'четверо суток')]"]
order_days_dropdown2 = [By.XPATH, "//*[starts-with(text(),'семеро суток')]"]
# поле Срок аренды после заполнения
order_days_selected = [By.XPATH, "//*[contains(@class,'Order_FilledDate__1pb8n')]//*[contains(@class,'Dropdown-placeholder')]"]
# поле Цвет самоката
order_color_black = [By.XPATH, "//*[@class = 'Checkbox_Label__3wxSf' and @for='black']"]  # черный
order_color_grey = [By.XPATH, "//*[@class = 'Checkbox_Label__3wxSf' and @for='grey']"]    # серый
# input поля Цвет самоката
order_color_black_input = [By.XPATH, "//*[@class = 'Checkbox_Input__14A2w' and @id = 'black']"]  # черный
order_color_grey_input = [By.XPATH, "//*[@class = 'Checkbox_Input__14A2w' and @id = 'grey']"]  # серый
# поле Комментарий для курьера
order_comment = [By.XPATH, '//*[@placeholder="Комментарий для курьера"]']
# кнопка Заказать
order_btn = [By.XPATH, "//*[@class = 'Order_Buttons__1xGrp']//*[text() = 'Заказать']"]
# кнопка Да всплывающего окна Хотяте оформить заказ?
order_btn_confirm = [By.XPATH, "//*[contains(@class,'Button_Button__ra12g') and text() = 'Да']"]
# заголовок окна Заказ оформлен
ordered_header = [By.XPATH, '//*[@class = "Order_ModalHeader__3FDaJ"]']
