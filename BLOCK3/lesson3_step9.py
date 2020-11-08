import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        driver = webdriver.Chrome()
        driver.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            driver.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        driver.quit()

def test_exception2():
    try:
        driver = webdriver.Chrome()
        driver.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            driver.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        driver.quit()