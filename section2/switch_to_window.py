from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_class_name("trollface")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = int(browser.find_element_by_id("input_value").text)
y = math.log(abs(12*math.sin(x)))
answer_field = browser.find_element_by_id("answer")
answer_field.send_keys(str(y))
button1 = browser.find_element_by_class_name("btn-primary")
button1.click()
button1.click()