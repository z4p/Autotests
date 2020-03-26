from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from random import choice

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
wait = WebDriverWait(driver,1000)
driver.get("https://adukar.by/")
element = driver.find_elements_by_class_name('masthead-menu__item_third')[1] #кнопка "Видеокурсы"
element.click()


# Выбор предмета
Items = driver.find_elements_by_class_name('subject-card') # кнопка списка предметов
def find_subject():
    return choice(Items)
	
random_subject = find_subject()
element = random_subject
print (element.text)
element.click()	

    


# проверка нумерации в уроке
def lesson_numbering(Lessons):
    List = Lessons.text  # вернули из кнопки текст урока
    Lesson_title_part = List.split() # разбили текст "УРОК N" на список
    if Lesson_title_part[0] == 'УРОК':
        Lesson_number = Lesson_title_part [1] # выделили из списка "УРОК N" номер урока
        Lessons.click()
        Link = driver.find_elements_by_tag_name('span')[41] # кнопка "Русский язык / Урок 1"
        Link_text = Link.text  # вернули текст "Русский язык / Урок 1"
        if len(Link_text)!= 0:
            Link_text_part = Link_text.split('/') # разбили текст "Русский язык / Урок 1" на список
            Next_lesson_title = Link_text_part[1].strip(' ') # выделили текст "Урок 1" 
            Next_lesson_number = Next_lesson_title.split() # разбили текст "Урок 1" на список отделив номер урока
            Numder = Next_lesson_number [1] #выделили номер урока
            if Numder == Lesson_number:
                return 'нумерация в названии и уроке совпадает'
            else:
                return 'нумерация в названии и уроке НЕ СОВПАДАЕТ!!!!!!!!!!!!!!!!!!'
            Link.click()
        else:
            return f'{List} в разработке'
    else:
        return f'работа {Lesson_title_part[0]}А проверяется отдельно'
	



Lesson_list = driver.find_elements_by_class_name('subject-number') #кнопка "УРОК N"

# работает только для 1го урока, дальше ошибку выдает
#for i in Lesson_list:
    #print (i.text)
    #result = lesson_numbering(i)
    #print (result)

# случайный выбор урока
def find_lessons():
    return choice(Lesson_list)

	
if len(Lesson_list) != 0:
    random_lesson_selection = find_lessons()
    print (random_lesson_selection.text)
    result = lesson_numbering(random_lesson_selection)
    print (result)
else:
    print ('предмет',element.text,'в разработке')	
    
   






# The End   
