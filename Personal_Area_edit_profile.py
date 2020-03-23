from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,5000)

Login = "BobushkaHI@mail.ru"
Password = "1111111111"
New_name_1 = "Bob"
New_name_2 = "Bobi"
New_password = '1111111110'
Image_1 = "C:\\Alla_work\\REPOSITORY\\Bob_1.jpg" # аватар_1
Image_2 = "C:\\Alla_work\\REPOSITORY\\Bob_2.jpg" # аватар_2

def Log_in (Pass):
    element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
    element.click()
    element = driver.find_element_by_name("email")
    element.send_keys(Login)
    element = driver.find_element_by_name("password")
    element.send_keys(Pass)
    element.send_keys(Keys.RETURN)
    element = driver.find_elements_by_class_name('icon-label')[1] #кнопка кабинет
    element.click()



def Edit_profile(name, Image, Pass, New_pass):
    element = driver.find_element_by_class_name('shepherd-cancel-link') #кнопка X
    element.click()
    element = driver.find_element_by_class_name('exit') #кнопка "Редактировать"
    element.click()
       
	# новое имя
    element = driver.find_element_by_class_name('input_large') #кнопка "Имя на сайте"
    element.clear()
    element.send_keys(name)	
    
	# добавление фото на аватар
    element = driver.find_element_by_class_name("input_hidden") #кнопка "Загрузить аватар"
    element.send_keys(Image)
    element = driver.find_elements_by_class_name('button_red')[4] #кнопка "Сохранить изменения"
    element.click()
    
	# смена пароля
    element = driver.find_elements_by_class_name('input_large')[1] #кнопка "Старый пароль"
    element.send_keys(Pass)
    element = driver.find_elements_by_class_name('input_large')[2] #кнопка "Новый пароль"
    element.send_keys(New_pass)
    element = driver.find_elements_by_class_name('button_red')[5] #кнопка "Сохранить пароль"
    element.click()

Log_in (Password)
print ('Поздравляю! Вы вошли в личный кабинет.')
Edit_profile(New_name_1, Image_1, Password, New_password)
print ("Данные успешно сохранены")
element = driver.find_elements_by_class_name('exit')[1] #кнопка "Выйти"
element.click()
Log_in (New_password)
print ("Вы повторно вошли в личный кабинет с измененными данными")


Edit_profile(New_name_2, Image_2, New_password, Password)
print ("Данные успешно сохранены")
element = driver.find_elements_by_class_name('exit')[1] #кнопка "Выйти"
element.click()
Log_in (Password)
print ("Вы еще раз вошли в личный кабинет с измененными данными")


assert "Страница не найдена" not in driver.page_source