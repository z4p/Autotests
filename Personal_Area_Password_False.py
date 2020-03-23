from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,500)

Login = "AlisaZeta@mail.ru"
Password_False = "CadY11111111"


def Log_in (Log, Pass):
    element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
    element.click()
    element = driver.find_element_by_name("email")
    element.send_keys(Log)
    element = driver.find_element_by_name("password")
    element.send_keys(Pass)
    element.send_keys(Keys.RETURN)
       

Log_in (Login, Password_False)
print ('Вы ввели неверный адрес электронной почты или пароль')

