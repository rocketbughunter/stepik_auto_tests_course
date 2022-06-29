
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
first_name_field = browser.find_element_by_name("firstname")
last_name_field = browser.find_element_by_name("lastname")
email_field = browser.find_element_by_name("email")
file_load_field = browser.find_element_by_name("file")
button = browser.find_element_by_class_name("btn-primary")
first_name_field.send_keys("Andrew")
last_name_field.send_keys("Platunov")
email_field.send_keys("testermail35@gmail.com")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '111.txt')
file_load_field.send_keys(file_path)
button.click()
