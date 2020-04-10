from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
import time
import webbrowser
driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
wait = WebDriverWait(driver,10)
driver.get("https://adukar.by/")

# после запуске надо изменить Email и Password в Log_in() (Email и Password взять из Video_courses_lesson_after_payment.py после его запуска)

def Log_in():
    Login = "e.vesnik2@mail.ru"
    Password = "BsrMEiGfh5"
    element = driver.find_elements_by_class_name('icon-label')[1] #кнопка войти
    element.click()
    time.sleep(1)
    element = driver.find_element_by_name("email")
    element.send_keys(Login)
    element = driver.find_element_by_name("password")
    element.send_keys(Password)
    element.send_keys(Keys.RETURN)

def Button_Videocourses():
    time.sleep(3)
    #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "masthead-menu__item_third")))
    element = driver.find_elements_by_class_name('masthead-menu__item_third')[1] #кнопка "Видеокурсы"
    button_video_courses = element.text  # выдает текст "Видеокурсы" и количество уроков
    text_button_video_courses = button_video_courses.split()
    text_video_courses = text_button_video_courses[0]
    print (text_video_courses) # печатает текст "Видеокурсы"
    element.click()
    

# случайный выбор предмета
def List_items():
    time.sleep(3)
    Items = driver.find_elements_by_class_name('subject-card') # кнопка списка предметов
    Lenght_Items = len(Items)
    Subject_selection = choice(Items)
    Subject_selection.click()
    Buttons = driver.find_elements_by_class_name('subject-number') # список уроков и тестов, нет атрибута текст  	
    Lenght_Objects = len(Buttons)
    if Lenght_Objects != 0:
        Sub = driver.find_element_by_tag_name('h1')
        print ('Предмет:',Sub.text)
    else:
        while Lenght_Objects == 0:
            Subject_selection = choice(Items)
            Subject_selection.click()
            Buttons = driver.find_elements_by_class_name('info') # список уроков и тестов и еще 4 кпоки  	
            Lenght_Objects = len(Buttons)
        Sub = driver.find_element_by_tag_name('h1')
        print ('Предмет:',Sub.text)	
	

# случайный выбор теста
def List_objects():
    time.sleep(3)
    Buttons_objects_1 = driver.find_elements_by_class_name('info') # список уроков и тестов и еще 4 кпоки, есть атрибут текст  	
    Lenght_buttons_objects_1 = len(Buttons_objects_1)
    Objects = []
    for i in range(4,Lenght_buttons_objects_1):	
        Objects.append(Buttons_objects_1[i])
    Object_selection = choice(Objects)
    Object_selection_text = Object_selection.text
    Lesson_or_test = Object_selection_text.split()
    if Lesson_or_test[0] == 'ТЕСТ':
        print (Object_selection.text)
        return Object_selection
    else:
        while Lesson_or_test[0] != 'ТЕСТ': 	
            Object_selection = choice(Objects)
            Object_selection_text = Object_selection.text
            Lesson_or_test = Object_selection_text.split()
        print (Object_selection.text)
        return Object_selection    

# доступ к тесту с авторизацией, произведение оплаты
def Access_test(Button_test):
    Button_test.click()
	
def After_payment_and_security():
    Button_phone = driver.find_element_by_name('phone')
    Button_phone.send_keys('79001234567')  # ввод номера телефона
    Button_send_code = driver.find_element_by_id('btnSendCode')
    Button_send_code.click()
    Button_sms_code = driver.find_element_by_name('sms_code')
    Button_sms_code.send_keys('554306')  # ввод смс кода
    Button_OK = driver.find_element_by_id('btnTestCode') 
    Button_OK.click()  #после нажатия вы войдете в тест



Log_in()
Button_Videocourses()
List_items() # выбор случайного предмета
random_Object = List_objects () # выбор случайного урока/теста
Access_test(random_Object)
After_payment_and_security()






#The End