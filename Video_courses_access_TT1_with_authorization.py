from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
import time
driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
wait = WebDriverWait(driver,10)
driver.get("https://adukar.by/")

# Открывает урок с авторизацией

def Log_in():
    Login = "vilas.gromov@mail.ru"
    Password = "rcvOn7BBrp"
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

# случайный выбор урока/теста
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
    if Lesson_or_test[0] == 'УРОК':
        Object_selection.click()
        Button_TT = driver.find_elements_by_class_name('test-button')  # класс ТТ1/ТТ2
        Lenght_button_TT = len(Button_TT)
        if Lenght_button_TT != 0:
            lesson_title = driver.find_elements_by_tag_name('h3')[0] # название урока
            print('Урок:',lesson_title.text)
            Button_TT1 = driver.find_elements_by_tag_name('a')[25]
            return Button_TT1
        else:
            while Lesson_or_test[0] == 'ТЕСТ' or Lenght_button_TT == 0:
                Object_selection = choice(Objects)
                Object_selection_text = Object_selection.text
                Lesson_or_test = Object_selection_text.split()
                Object_selection.click()
                Button_TT = driver.find_elements_by_class_name('test-button')  # класс ТТ1/ТТ2
                Lenght_button_TT = len(Button_TT)
            lesson_title =  driver.find_elements_by_tag_name('h3')[0] # название урока
            print('Урок:',lesson_title.text)
            Button_TT1 = driver.find_elements_by_tag_name('a')[25]
            return Button_TT1
    else:
        while Lesson_or_test[0] != 'УРОК': 	
            Object_selection = choice(Objects)
            Object_selection_text = Object_selection.text
            Lesson_or_test = Object_selection_text.split()
        Object_selection.click()
        Button_TT = driver.find_elements_by_class_name('test-button')  # класс ТТ1/ТТ2
        Lenght_button_TT = len(Button_TT)
        if Lenght_button_TT != 0:
            lesson_title = driver.find_elements_by_tag_name('h3')[0] # название урока
            print('Урок:',lesson_title.text)
            Button_TT1 = driver.find_elements_by_tag_name('a')[25]
            return Button_TT1
        else:
            while Lesson_or_test[0] == 'ТЕСТ' or Lenght_button_TT == 0:
                Object_selection = choice(Objects)
                Object_selection_text = Object_selection.text
                Lesson_or_test = Object_selection_text.split()
                Object_selection.click()
                Button_TT = driver.find_elements_by_class_name('test-button')  # класс ТТ1/ТТ2
                Lenght_button_TT = len(Button_TT)
            lesson_title =  driver.find_elements_by_tag_name('h3')[0] # название урока
            print('Урок:',lesson_title.text)
            Button_TT1 = driver.find_elements_by_tag_name('a')[25]
            return Button_TT1

def Access_test(Button_test):
    Button_test.click()



Log_in()
Button_Videocourses()
List_items() # выбор случайного предмета
random_lesson = List_objects () # выбор случайного урока/теста
Access_test(random_lesson )



# The End
