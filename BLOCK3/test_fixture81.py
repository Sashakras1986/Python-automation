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

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("regression test started")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("regression test finished")
    # для запуска только смоук тестов в Win10 нужно использовать логическое 'и':
    # pytest -s -v -m "smoke and win10" test_fixture81.py
