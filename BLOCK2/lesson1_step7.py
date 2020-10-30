import math
from selenium import webdriver
import time
# функиця расчета выражения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # поиск элемента и получение значения атрибута
    treasure = driver.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    # расчеты c отправкой значения в функцию calc
    y = calc(x)
    # отправка ответа в поле ввода
    answer = driver.find_element_by_id("answer")
    answer.send_keys(y)
    # работа с чекбоксом и радио
    check = driver.find_element_by_id("robotCheckbox")
    check.click()
    radio = driver.find_element_by_id("robotsRule")
    radio.click()
    time.sleep(1)
    button = driver.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла