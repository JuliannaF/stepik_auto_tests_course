import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
   link = "http://suninjuly.github.io/execute_script.html"
   browser = webdriver.Chrome()
   browser.get(link)

   x_element = browser.find_element(By.ID, "input_value")
   x = x_element.text
   def calc(x):
     return str(math.log(abs(12 * math.sin(int(x)))))
   y = calc(x)

   input1 = browser.find_element(By.ID, "answer")
   input1.send_keys(y)

   browser.execute_script("window.scrollBy(0, 1000);")

   option1 = browser.find_element(By.ID, "robotCheckbox")
   option1.click()
   option2 = browser.find_element(By.ID, "robotsRule")
   option2.click()

   button = browser.find_element(By.CSS_SELECTOR, "button.btn")
   button.click()

finally:
   # успеваем скопировать код за 30 секунд
   time.sleep(10)
   # закрываем браузер после всех манипуляций
   browser.quit()