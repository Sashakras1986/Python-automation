from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    driver = webdriver.Chrome()
    driver.get(link)
    # button = driver.find_element_by_id("submit_button")
    button = driver.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(2)
# закрываем браузер
finally:
    driver.quit()