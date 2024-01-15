import unittest
class TestAbs(unittest.TestCase):
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Julia")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Furmanova")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("ula55509@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()