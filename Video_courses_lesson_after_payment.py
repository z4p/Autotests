from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
import time
driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
wait = WebDriverWait(driver,10)
driver.get("https://adukar.by/")

# после запуска надо изменить Email и Password в Log_in() (зарегистировать нового пользователя), а Email и Password сохранить для Video_courses_lesson_after_payment.py

def Log_in():
    Login = "vilas.gromov6@mail.ru"
    Password = "Kn1JX0Hy27"
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
    Items = []
    First_subject = driver.find_elements_by_class_name('subject-card')[0] # кнопка Русский язык
    Second_subject = driver.find_elements_by_class_name('subject-card')[1] # кнопка Беларусский язык
    Items.append(First_subject)
    Items.append(Second_subject)
    Subject_selection = choice(Items)
    print('Предмет:',Subject_selection.text)
    Subject_selection.click()

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


# доступ к тесту с авторизацией
def Access_test(Button_test):
    Button_test.click()
    

# выполнение оплаты
def After_payment():
    link_name = driver.find_element_by_id('testPurchaseBtn').get_attribute("href") # ссылка на оплату
    driver.get(link_name) # ссылка на оплату открывается в новом окне
    Button_promocode = driver.find_element_by_id('promocode')
    Button_promocode.send_keys('Gsudjcjp3')
    Button_apply = driver.find_element_by_id('applyPromocode')
    Button_apply.click()
    Button_video_courses = driver.find_elements_by_class_name('masthead-menu__item_third')[1] #кнопка "Видеокурсы
    Button_video_courses.click()
    List_items() # выбор случайного предмета
    random_Object = List_objects () # выбор случайного урока
    Access_test(random_Object)

Log_in()
Button_Videocourses()
List_items() # выбор случайного предмета
random_Object = List_objects () # выбор случайного урока
Access_test(random_Object)
After_payment()








# The End
