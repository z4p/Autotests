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

# вконце надо раскаментировать кнопку "Применить", чтобы произвести оплату

def Log_in():
    Login = "vilas.gromov3@mail.ru"
    Password = "ol4pOom6LP"
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
    

# случайный выбор предмета (Русский язык/Беларусский язык)
def List_items():
    time.sleep(3)
    Items = []
    First_subject = driver.find_elements_by_class_name('subject-card')[0] # кнопка Русский язык
    Second_subject = driver.find_elements_by_class_name('subject-card')[1] # кнопка Беларусский язык
    Items.append(First_subject)
    Items.append(Second_subject)
    Subject_selection = choice(Items)
    print('Предмет:',Subject_selection.text)
    Subject_selection.click()
	

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
    Button_payment = driver.find_element_by_id('testPurchaseBtn')
    Button_payment.click()
    driver.close()
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        Button_promocode = driver.find_elements_by_class_name('input')[0]		
        Button_promocode.send_keys('Gsudjcjp3')
		# Button_apply = driver.find_element_by_id('applyPromocode')
        # Button_apply.click() после нажатия оплата будет произведена



Log_in()
Button_Videocourses()
List_items() # выбор случайного предмета
random_Object = List_objects () # выбор случайного урока/теста
Access_test(random_Object)







#The End