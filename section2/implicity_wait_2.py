from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element(By.ID, 'book')
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button.click()
x = int(browser.find_element_by_id("input_value").text)
y = math.log(abs(12 * math.sin(x)))
answer = browser.find_element_by_id("answer")
answer.send_keys(str(y))
button1 = browser.find_element(By.ID, 'solve')
button1.click()
