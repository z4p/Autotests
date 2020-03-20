from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,1000)

Login = "AlisaZeta@mail.ru"
Password = "CadYyqrqMn"

element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
element.click()
element = driver.find_element_by_name("email")
element.send_keys(Login)
element = driver.find_element_by_name("password")
element.send_keys(Password)
element.send_keys(Keys.RETURN)
element = driver.find_elements_by_class_name('icon-label')[1] #кнопка кабинет
element.click()
element = driver.find_element_by_class_name('shepherd-cancel-link') #кнопка X
element.click()
print ('Поздравляю! Вы вошли в личный кабинет.')
element = driver.find_elements_by_class_name('item')[1] #кнопка Высшие учебные заведения
element.click()


print ('Вы находитесь в разделе "ЦТ онлайн"')
print ('Проверить отображение следующей информации:')
print('                             * текст "Выбирай предмет и готовься к ЦТ бесплатно!"')
print('                             * список предметов в виде плиток: Русский язык, Белорусский язык, Математика, Английский язык, Физика, Химия, Биология, Обществоведение, История Беларуси ')


assert "Страница не найдена" not in driver.page_source