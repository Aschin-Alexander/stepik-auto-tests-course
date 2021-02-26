from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    f_num1 = browser.find_element_by_id("num1")
    num1 = int(f_num1.text)
    f_num2 = browser.find_element_by_id("num2")
    num2 = int(f_num2.text)
    sum_nums = num1 + num2
    f_select = Select(browser.find_element_by_class_name("custom-select"))
    f_select.select_by_value(str(sum_nums))
    f_btn = browser.find_element_by_class_name("btn")
    f_btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()