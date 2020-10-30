import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# функиця расчета выражения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # расчеты
    x_element = driver.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    # отправка ответа в поле ввода
    fname = driver.find_element_by_id("answer")
    fname.send_keys(y)
    # работа с чекбоксом и радио
    check = driver.find_element_by_css_selector("[for='robotCheckbox']")
    check.click()
    radio = driver.find_element_by_css_selector("[for='robotsRule']")
    radio.click()
    time.sleep(1)
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла