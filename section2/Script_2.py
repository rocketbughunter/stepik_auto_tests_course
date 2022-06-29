from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = int(browser.find_element_by_id("input_value").text)
    y = math.log(abs(12 * math.sin(x)))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))
    button = browser.find_element(By.TAG_NAME, "button")
    browser.find_element_by_id("robotCheckbox").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id("robotsRule").click()
    button.click()

finally:
    time.sleep(15)
    browser.quit()