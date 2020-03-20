from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,100)

Login = "Suny1111@mail.ru"  #пароль для входа в эл почту 98*98*98


element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
element.click()
element = driver.find_element_by_name("email")
element.send_keys(Login)
element = driver.find_element_by_class_name("input-item__button") #кнопка не помню
element.click()
element = driver.find_elements_by_name("email")[2]
element.send_keys(Login)
element = driver.find_elements_by_class_name("button_red")[2] #кнопка Восстановить пароль
element.click()
element = driver.find_elements_by_class_name("button_red")[3] #кнопка Перейти на главную страницу
element.click()
element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
element.click()
element = driver.find_element_by_name("email")
element.send_keys(Login)
print('Введите пароль высланный на адрес электронной почты:',Login)
print ('Нажать на кнопку "Войти"')
print ('Поздравляю! Вы только что восстановили пароль с помощью электронной почты)')



assert "Страница не найдена" not in driver.page_source

