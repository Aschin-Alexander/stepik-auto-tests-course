from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    f_num1 = browser.find_element_by_id("input_value")
    num1 = int(f_num1.text)
    f_answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", f_answer)
    f_answer.send_keys(calc(num1))
    f_checkbox = browser.find_element_by_id("robotCheckbox")
    f_checkbox.click()
    f_radiobtn = browser.find_element_by_id("robotsRule")
    f_radiobtn.click()
    f_btn = browser.find_element_by_class_name("btn")
    f_btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()