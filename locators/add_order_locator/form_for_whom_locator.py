from selenium.webdriver.common.by import By

# форма Для кого самокат

# поле Имя
order_name = [By.XPATH, '//*[@placeholder="* Имя"]']
# поле Фамилия
order_surname = [By.XPATH, '//*[@placeholder="* Фамилия"]']
# поле Адрес: куда привезти заказ
order_address = [By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]']
# поле Станция метро
order_metro = [By.XPATH, '//*[@placeholder="* Станция метро"]']
# поле Станция метро в выпадающем списке
order_metro_dropdown1 = [By.XPATH, "//*[starts-with(text(),'Маяковская')]"]
order_metro_dropdown2 = [By.XPATH, "//*[starts-with(text(),'Красносельская')]"]
# поле Телефон: на него позвонит курьер
order_phone = [By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]']
# кнопка Далее
form_for_whom_next_btn = [By.XPATH, "//*[contains(@class,'Button_Button__ra12g') and text() = 'Далее']"]