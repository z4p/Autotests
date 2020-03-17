from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,200)

# информация для ввода данных в поле ввода:
Email = "AlisaZeta@mail.ru"
Password = "98*98*98"


element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
element.click()
element = driver.find_elements_by_class_name('form__text_accent')[1]#кнопка регистрация
element.click()
element = driver.find_elements_by_class_name('social-button__text')[2]#кнопка VK
element.click()
element = driver.find_elements_by_class_name('oauth_form_input')[0]# поле ввода еmail в VK
element.send_keys(Email)
element = driver.find_elements_by_class_name("oauth_form_input")[1]#поле ввода pass в VK
element.send_keys(Password)
element = driver.find_element_by_class_name('oauth_button')#кнопка войти в VK
element.click()
element = driver.find_element_by_class_name('button_indent')#кнопка разшешить по доступу к аккаунту в VK
element.click()
assert "Страница не найдена" not in driver.page_source
element.clear()
driver.close()