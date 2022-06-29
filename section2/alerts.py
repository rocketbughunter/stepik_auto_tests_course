from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_class_name("btn-primary")
button.click()
confirm = browser.switch_to.alert
confirm.accept()
x = int(browser.find_element_by_id("input_value").text)
y = math.log(abs(12*math.sin(x)))
answer_field = browser.find_element_by_id("answer")
answer_field.send_keys(str(y))
button = browser.find_element_by_class_name("btn-primary")
button.click()
