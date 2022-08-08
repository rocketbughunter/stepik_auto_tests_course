import unittest
from selenium import webdriver

class TestAbs(unittest.TestCase):

    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('//input[contains(@placeholder, "Input your first name")]')
        input1.send_keys('Andrew')
        input2 = browser.find_element_by_xpath(('//input[contains(@placeholder, "Input your last name")]'))
        input2.send_keys('Petrov')
        input3 = browser.find_element_by_xpath(('//input[contains(@placeholder, "Input your email")]'))
        input3.send_keys('andrew@ya.ru')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('//input[contains(@placeholder, "Input your first name")]')
        input1.send_keys('Andrew')
        input2 = browser.find_element_by_xpath(('//input[contains(@placeholder, "Input your last name")]'))
        input2.send_keys('Petrov')
        input3 = browser.find_element_by_xpath(('//input[contains(@placeholder, "Input your email")]'))
        input3.send_keys('andrew@ya.ru')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__": unittest.main()

