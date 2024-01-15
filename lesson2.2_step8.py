from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name=firstname]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name=lastname]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name=email]")
    input3.send_keys("ula55509@mail.ru")

    with open('test1.txt', 'w') as file:
        file.write('test1 for mls 228')

    import os  # импортируем модуль

    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого скрипта lesson2_8.py

    file_name = "test1.txt"    # имя файла, который будем загружать на сайт

    file_path = os.path.join(current_dir, file_name)    # получаем путь к file_example.txt

    element = browser.find_element(By.ID,'file')
    element.send_keys(file_path)  # отправляем файл

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла