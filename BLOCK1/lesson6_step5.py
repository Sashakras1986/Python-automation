import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

page = "http://suninjuly.github.io/find_link_text"

try:
    driver = webdriver.Chrome()
    driver.get(page)
    link = driver.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Alex")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("K")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Spb")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла