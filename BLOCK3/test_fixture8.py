import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        print("smoke test started")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("smoke test finished")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("regression test started")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("regression test finished")
