from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,200)

# данные для ввода:
Email = "AlisaZeta@mail.ru"
Name = "Alisa"

element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
element.click()
element = driver.find_elements_by_class_name('form__text_accent')[1]#кнопка регистрация
element.click()
element = driver.find_elements_by_class_name("input")[2]#поле ввода"эл почта"
element.send_keys(Email)
element = driver.find_elements_by_class_name("input")[3]#поле ввода "имя на сайте"
element.send_keys(Name)
element = driver.find_elements_by_class_name('button_red')[1]#кнопка зарегистрироваться
element.click()
element = driver.find_elements_by_class_name('button_red')[3]#кнопка перейти на главную страницу
element.click()
assert "Страница не найдена" not in driver.page_source
element.clear()
driver.close()


