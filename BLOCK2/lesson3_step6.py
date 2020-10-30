from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    # запоминаем имя текущей вкладки на свякий случай
    first_window = driver.window_handles[0]
    # нажимаем на кнопку на странице
    button = driver.find_element_by_class_name("btn").click()
    # запоминаем имя второй вкладки и переходим в нее
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    # забираем x и отправляем его для рассчета в функцию
    x = driver.find_element_by_id("input_value").text
    y = calc(x)
    # ищем поле ввода и вводим туда ответ математического выражения
    answer = driver.find_element_by_id("answer").send_keys(y)
    # ищем кнопку и нажимаем на нее
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
    driver.get('https://stepik.org/lesson/184253/step/6?unit=158843')
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