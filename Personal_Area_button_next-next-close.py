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
print ('Поздравляю! Вы вошли в личный кабинет.')

element = driver.find_elements_by_class_name('shepherd-button-example-primary')[0] #кнопка Дальше
element.click()
print ('Нажата кнопка "Далее" в модальном окне "Панель навигации"')
element = driver.find_elements_by_class_name('shepherd-button-example-primary')[1] #кнопка Дальше
element.click()
print ('Нажата кнопка "Далее" в модальном окне "Успеваемость"')
element = driver.find_elements_by_class_name('shepherd-button-example-primary')[2] #кнопка Закрыть
element.click()
print ('Нажата кнопка "Закрыть" в модальном окне "Специальности"')

print ('Проверить следущую информацию:')
print ('                             * Имя пользователя такое же как было введено при регистрации')
print ('                             * Наличие кнопок "редактировать/выйти"')
print ('                             * раздел: ЦЕНТРАЛИЗОВАННОЕ ТЕСТИРОВАНИЕ')
print ('                                 - кнопка "Мои Цели')
print ('                                 - кнопка "ЦТ онлайн')
print ('                             * раздел: ИЗБРАННОЕ')
print ('                                 - кнопка "Высшие учебные заведения"')
print ('                                 - кнопка "Колледжи и лицеи"')


assert "Страница не найдена" not in driver.page_source