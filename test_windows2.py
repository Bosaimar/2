from selenium import webdriver
import time
import math
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

try:
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100")
    button2 = browser.find_element_by_id("book")
    button2.click()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(int(x))
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button1 = browser.find_element_by_xpath("//button[text()='Submit']")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла