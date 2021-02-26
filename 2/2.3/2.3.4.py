from selenium import webdriver
import time, math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_class_name("btn").click()
    time.sleep(2)
    confirm1 = browser.switch_to_alert()
    confirm1.accept()
    time.sleep(2)
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_class_name("btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
