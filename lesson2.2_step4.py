from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.execute_script("document.title='Script executing';alert('Robots at work');")

time.sleep(10)

# Метод execute_script

# С помощью метода execute_script можно выполнить программу,
# написанную на языке JavaScript, как часть сценария автотеста в запущенном браузере.