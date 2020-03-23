from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,1000)

Login = "AlisaZeta@mail.ru"
Password = "CadYyqrqMn"

def Log_in (Log, Pass):
    element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
    element.click()
    element = driver.find_element_by_name("email")
    element.send_keys(Log)
    element = driver.find_element_by_name("password")
    element.send_keys(Pass)
    element.send_keys(Keys.RETURN)
    element = driver.find_elements_by_class_name('icon-label')[1] #кнопка кабинет
    element.click()
    element = driver.find_element_by_class_name('shepherd-cancel-link') #кнопка X
    element.click()

Log_in (Login, Password)
print ('Поздравляю! Вы вошли в личный кабинет.')
element = driver.find_elements_by_class_name('exit')[1] #кнопка "Выйти"
element.click()
print ('Вы вышли из личного кабинета')
Log_in (Login, Password)
print ('И снова вошли в личный кабинет')
