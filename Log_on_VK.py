from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,100)
Login = "AlisaZeta@mail.ru"
Password = "98*98*98"
element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
element.click()
element = driver.find_elements_by_class_name('social-button__text')[0]#кнопка VK
element.click()
element = driver.find_elements_by_class_name('oauth_form_input')[0]# поле ввода еmail в VK
element.send_keys(Login)
element = driver.find_elements_by_class_name("oauth_form_input")[1]#поле ввода pass в VK
element.send_keys(Password)
element.send_keys(Keys.RETURN)
element = driver.find_elements_by_class_name('icon-label')[1] #кнопка кабинет
element.click()
print ('Поздравляю! Вы вошли в личный кабинет.')
assert "Страница не найдена" not in driver.page_source
element.clear()
driver.close()
