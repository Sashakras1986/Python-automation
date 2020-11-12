import pytest
from selenium import webdriver
import time
import math

def calc():
    answer = str(math.log(int(time.time())))
    return answer

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

# class TestMainPage1():

def test_lesson_236895(browser):
    browser.implicitly_wait(10)
    browser.get("https://stepik.org/lesson/236895/step/1")
    browser.find_element_by_css_selector("textarea").send_keys(calc())
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(5)
    #pre.smart - hints__hint