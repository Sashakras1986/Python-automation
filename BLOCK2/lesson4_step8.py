from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    # ловим цену $100
    price_catch = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    book = driver.find_element_by_id("book").click()
    #  находим кнопку submit и скроллим вниз до неё
    submit = driver.find_element_by_id("solve")
    driver.execute_script("return arguments[0].scrollIntoView(true);", submit)
    # забираем x и отправляем его для рассчета в функцию
    x = driver.find_element_by_id("input_value").text
    y = calc(x)
    # ищем поле ввода и вводим туда ответ математического выражения
    answer = driver.find_element_by_id("answer").send_keys(y)
    # ищем кнопку и нажимаем на нее
    submit.click()
    # парсим ответ из alert
    alert = driver.switch_to.alert
    alert_text = alert.text.split()
    alert.accept()
    answer = alert_text[-1]
    # идем на Степик
    driver.get('https://stepik.org/catalog?auth=login&language=ru')
    time.sleep(5)
    # логинимся
    driver.find_element_by_id('id_login_email').send_keys('sasha.kras1986@gmail.com')  # здесь вводится e-mail
    driver.find_element_by_id('id_login_password').send_keys('Stepik151118')  # здесь вводится пароль
    driver.find_element_by_class_name('sign-form__btn').click()
    time.sleep(3)
    # идем на страницу задачи
    driver.get('https://stepik.org/lesson/181384/step/8?unit=156009')
    time.sleep(7)
    # находим поле ввода и постим ответ
    answer_input = driver.find_element_by_css_selector("textarea")
    driver.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(answer)
    # находим кнопку отправки и нажимаем на нее
    button = driver.find_element_by_class_name('submit-submission')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()