from selenium import webdriver
import os
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/alert_accept.html")
    # нажимаем на кнопку на странице
    button = driver.find_element_by_class_name("btn").click()
    # нажимаем на на кнопку ОК в alert
    confirm = driver.switch_to.alert.accept()
    # забираем x и отправляем его для рассчета в функцию
    x = driver.find_element_by_id("input_value").text
    y = calc(x)
    # ищем поле ввода и постим туда ответ математического выражения
    answer = driver.find_element_by_id("answer").send_keys(y)
    # ищем кнопку и нажимаем ее
    button = driver.find_element_by_tag_name("button").click()
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
    driver.get('https://stepik.org/lesson/184253/step/4?unit=158843')
    time.sleep(3)
    # находим поле ввода и постим ответ
    answer_input = driver.find_element_by_css_selector('textarea')
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