import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


# запуск с маркировкой из терминала pytest -s -v -m smoke test_fixture8.py выполнятся только те что промаркированы в смоук
# запуск с маркировкой НЕ смоук pytest -s -v -m "not smoke" test_fixture8.py
# запуск с макировкой смоук или регресс pytest -s -v -m "smoke or regression" test_fixture8.py