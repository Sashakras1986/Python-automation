from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    fname = driver.find_element_by_css_selector("input[placeholder='Input your first name']")
    fname.send_keys("Robo")
    lname = driver.find_element_by_css_selector("input[placeholder='Input your last name']")
    lname.send_keys("Robotest")
    lname = driver.find_element_by_css_selector("input[placeholder='Input your email']")
    lname.send_keys("robo@robomail.com")
    time.sleep(1)
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)
    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name('h1')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла