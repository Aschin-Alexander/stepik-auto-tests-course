from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration2.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()


class TestReg(unittest.TestCase):

    # Ваш код, который заполняет обязательные поля
    def testing(self, link):
        browser.get(link)
        if browser.current_url == None: return "bad"
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block .second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block .third")
        input3.send_keys("Ivanov@ivan.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block .first")
        input4.send_keys("88005553535")
        input5 = browser.find_element(By.CSS_SELECTOR, "div.second_block .second")
        input5.send_keys("far far away")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        time.sleep(10)
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        unittest.TestCase.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        if __name__ == "__main__":
            unittest.main()


test1 = TestReg.testing(link1)

test2 = TestReg.testing(link2)

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
