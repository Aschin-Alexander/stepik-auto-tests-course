from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    f_treasure = browser.find_element_by_id("treasure")
    x_value = f_treasure.get_attribute("valuex")
    y = calc(x_value)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    f_checkbox = browser.find_element_by_id("robotCheckbox")
    f_checkbox.click()
    f_radiobtn = browser.find_element_by_id("robotsRule")
    f_radiobtn.click()
    f_btn = browser.find_element_by_class_name("btn")
    f_btn.click()

finally:
    time.sleep(10)
    browser.quit()
