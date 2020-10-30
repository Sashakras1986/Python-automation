from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    # заполняем поля ввода
    fname = driver.find_element_by_css_selector("input[placeholder='Enter first name']")
    fname.send_keys("Robo")
    lname = driver.find_element_by_css_selector("input[placeholder='Enter last name']")
    lname.send_keys("Robotest")
    lname = driver.find_element_by_css_selector("input[placeholder='Enter email']")
    lname.send_keys("robo@robomail.com")
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'test.txt')
    # находим кнопку загрузки файла
    upload = driver.find_element_by_id("file")
    upload.send_keys(file_path)
    button = driver.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()