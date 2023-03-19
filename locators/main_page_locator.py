from selenium.webdriver.common.by import By

# элементы вопросов
question_0 = [By.ID, 'accordion__heading-0']
question_1 = [By.ID, 'accordion__heading-1']
question_2 = [By.ID, 'accordion__heading-2']
question_3 = [By.ID, 'accordion__heading-3']
question_4 = [By.ID, 'accordion__heading-4']
question_5 = [By.ID, 'accordion__heading-5']
question_6 = [By.ID, 'accordion__heading-6']
question_7 = [By.ID, 'accordion__heading-7']
# элементы ответов на вопросы (чтобы проверять hidden)
answer_0_div = [By.XPATH, "//*[@aria-labelledby='accordion__heading-0']"]
answer_1_div = [By.XPATH, "//*[@aria-labelledby='accordion__heading-1']"]
answer_2_div = [By.XPATH, "//*[@aria-labelledby='accordion__heading-2']"]
answer_3_div = [By.XPATH, "//*[@aria-labelledby='accordion__heading-3']"]
answer_4_div = [By.XPATH, "//*[@aria-labelledby='accordion__heading-4']"]
answer_5_div = [By.XPATH, "//*[@aria-labelledby='accordion__heading-5']"]
answer_6_div = [By.XPATH, "//*[@aria-labelledby='accordion__heading-6']"]
answer_7_div = [By.XPATH, "//*[@aria-labelledby='accordion__heading-7']"]
# элементы с текстом ответов
answer_0_p = [By.XPATH, "//*[@aria-labelledby='accordion__heading-0']//p"]
answer_1_p = [By.XPATH, "//*[@aria-labelledby='accordion__heading-1']//p"]
answer_2_p = [By.XPATH, "//*[@aria-labelledby='accordion__heading-2']//p"]
answer_3_p = [By.XPATH, "//*[@aria-labelledby='accordion__heading-3']//p"]
answer_4_p = [By.XPATH, "//*[@aria-labelledby='accordion__heading-4']//p"]
answer_5_p = [By.XPATH, "//*[@aria-labelledby='accordion__heading-5']//p"]
answer_6_p = [By.XPATH, "//*[@aria-labelledby='accordion__heading-6']//p"]
answer_7_p = [By.XPATH, "//*[@aria-labelledby='accordion__heading-7']//p"]
# логотип: надпись Самокат
logo_scooter = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
# логотип: надпись Яндекс
logo_yandex = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

