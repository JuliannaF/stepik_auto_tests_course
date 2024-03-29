from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
x = int(x_element.text)

y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
y = int(y_element.text)

select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
select.select_by_value(str(x+y))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла

