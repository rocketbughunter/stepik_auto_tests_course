from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    z = int(x)+int(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))
    browser.find_element_by_css_selector('[class="btn btn-default"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()