import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(n1,n2):
  return str(n1 + n2)
# код прекрасно работает на обеих линках
link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    num1 = driver.find_element_by_id("num1")
    n1 = int(num1.text)
    num2 = driver.find_element_by_id("num2")
    n2 = int(num2.text)
    sum = calc(n1,n2)
    print(n1, '+', n2,'=', sum)
    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    button = driver.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла