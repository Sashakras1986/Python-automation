import math
from selenium import webdriver
import time

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    # забираем x и отправляем его для рассчета в функцию
    xt = driver.find_element_by_id("input_value")
    x = int(xt.text)
    y = calc(x)
    # ищем поле ввода и постим туда ответ математического выражения
    answer = driver.find_element_by_id("answer")
    answer.send_keys(y)
    check = driver.find_element_by_id("robotCheckbox")
    driver.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    # ищем радиобокс и скроллим его, чтобы попал в область видимости
    radio = driver.find_element_by_id("robotsRule")
    driver.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    # ищем кнопку и скроллим ее, чтобы попала в область видимости
    button = driver.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()