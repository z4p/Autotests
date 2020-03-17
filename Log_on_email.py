from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,100)

Login = "Fomawork10@mail.ru"
Password = "1111111111"

element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
element.click()
element = driver.find_element_by_name("email")
element.send_keys(Login)
element = driver.find_element_by_name("password")
element.send_keys(Password)
element.send_keys(Keys.RETURN)
assert "Страница не найдена" not in driver.page_source
element.clear()
driver.close()