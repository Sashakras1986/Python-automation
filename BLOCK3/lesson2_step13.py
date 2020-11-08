from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestUn(unittest.TestCase):
    def test_un1(self):
        driver = webdriver.Chrome()
        driver.get("http://suninjuly.github.io/registration1.html")
        fname = driver.find_element_by_css_selector("input[placeholder='Input your first name']")
        fname.send_keys("Robo")
        lname = driver.find_element_by_css_selector("input[placeholder='Input your last name']")
        lname.send_keys("Robotest")
        lname = driver.find_element_by_css_selector("input[placeholder='Input your email']")
        lname.send_keys("robo@robomail.com")
        time.sleep(1)
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = driver.find_element_by_tag_name('h1')
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "not equal")
        driver.quit()

    def test_un2(self):
        driver = webdriver.Chrome()
        driver.get("http://suninjuly.github.io/registration2.html")
        fname = driver.find_element_by_css_selector("input[placeholder='Input your first name']")
        fname.send_keys("Robo")
        lname = driver.find_element_by_css_selector("input[placeholder='Input your last name']")
        lname.send_keys("Robotest")
        lname = driver.find_element_by_css_selector("input[placeholder='Input your email']")
        lname.send_keys("robo@robomail.com")
        time.sleep(1)
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = driver.find_element_by_tag_name('h1')
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "not equal")

if __name__ == "__main__":
    unittest.main()