from selenium import webdriver
import time, math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(12)

    wait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_id("book").click()

    x = browser.find_element_by_id("input_value").text
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_id("answer"))
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_id("solve").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
