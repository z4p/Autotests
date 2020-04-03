from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from random import choice
import time  # модуль для задержки времени

# Запускать несколько раз. Открывает тесты/уроки(проверочный тест 1 в уроке)

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
wait = WebDriverWait(driver,1000)
driver.get("https://adukar.by/")
element = driver.find_elements_by_class_name('masthead-menu__item_third')[1] #кнопка "Видеокурсы"
button_video_courses = element.text  # выдает текст "Видеокурсы" и количество уроков
text_button_video_courses = button_video_courses.split()
text_video_courses = text_button_video_courses[0]
print (text_video_courses) # печатает текст "Видеокурсы"
element.click()


# случайный выбор предмета
def List_items():
    Items = driver.find_elements_by_class_name('subject-card') # кнопка списка предметов
    Subject_selection = choice(Items)
    print ('Предмет:',Subject_selection.text)
    return Subject_selection

# случайная кнопка из списка уроков/тестов по предмету 
def List_objects(Subject):
    Subject.click()
    Number_lessons_tests = driver.find_elements_by_class_name('subject-number') # список уроков и тестов
    Buttons = driver.find_elements_by_class_name('info') # список уроков и тестов и еще 4 кпоки  	
    Lenght_Objects = len(Buttons)
    Objects = []
    print ('Kол-во уроков/тестов:',len(Number_lessons_tests))
    for i in range(4,Lenght_Objects):	
        Objects.append(Buttons[i])
    if Lenght_Objects != 0:
        Object_selection = choice(Objects)
        print ("Название урока/теста: \n"+Object_selection.text)
        return Object_selection
    else:
        return f'Предмет находится в разработке'
   
    
	
# доступ к уроку/тесту без авторизации
def Access_lesson_or_test(random_Object):
    if random_Object == 'Предмет находится в разработке':
        return 'Предмет находится в разработке'
    else:
        Text_random_Object = random_Object.text
        frist_word_random_Object = Text_random_Object.split()
        if frist_word_random_Object[0] == 'ТЕСТ':
            random_Object.click()
            return 'Вы сможете войти в тест только после регистрации'
        elif frist_word_random_Object[0] == 'УРОК':
            random_Object.click()
            Button_TT = driver.find_elements_by_class_name('test-button')  # класс ТТ1/ТТ2
            Lenght_button_TT = len(Button_TT)
            if Lenght_button_TT == 0:
                return 'Урок находится в разработке.'
            else: 
                Button_TT1 = driver.find_elements_by_tag_name('a')[25]
                Button_TT1.click()
                return 'Поздравляю! Вы вошли в урок \n'+'Для того, чтобы пройти тренировочный тест 1, необходимо зарегистрироваться'
   
    


random_subject = List_items() # выбор случайного предмета
random_Objects = List_objects (random_subject) # выбор случайного урока/теста
result = Access_lesson_or_test(random_Objects) #нажатие на выбранный тест/урок
print (result)







#The end
