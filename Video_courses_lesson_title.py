from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from random import choice

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
wait = WebDriverWait(driver,10000)
driver.get("https://adukar.by/")
element = driver.find_elements_by_class_name('masthead-menu__item_third')[1] #кнопка "Видеокурсы"
button_video_courses = element.text  # выдает текст "Видеокурсы" и количество уроков
text_button_video_courses = button_video_courses.split()
text_video_courses = text_button_video_courses[0]
print (text_video_courses) # печатает текст "Видеокурсы"
element.click()


# случайный выбор предмета
def Subject_selection():
    Items = driver.find_elements_by_class_name('subject-card') # кнопка списка предметов
    return choice(Items)


# спискок "Название урока"
def Lesson_list():
    Lesson_title_list = []
    Lesson_list = driver.find_elements_by_class_name('info') #кнопка "УРОК N" и название и еще что-то
    Length = len(Lesson_list)
    if Length > 0: 
        for i in range(4,Length):
            List = Lesson_list[i].text
            New_list = List.split()  # разбили на списки, разделив каждое слово
            if New_list[0] == 'УРОК':
                New_list.pop(0) #удалили первое слово из списка "Урок"
                New_list.pop(0) #удалили второе слово из списка № Урока
                List_of_lesson_title = ' '.join(New_list) #объединили слова из названия урока в список из названия уроков 
                Lesson_title_list.append(List_of_lesson_title)
        return Lesson_title_list
          			


# случайный выбор урока
def Lesson_selection():
    Lessons = Lesson_list() # список уроков
    return choice(Lessons)


# проверка названия урока и предмета урока из списка с названием самого урока и названием видеоурока
def Lesson_title(Lesson, item_name):
    Lesson_list_1 = driver.find_elements_by_class_name('info') #кнопка "УРОК N" и название и еще что-то
    Length_1 = len(Lesson_list_1)
    if Length_1 > 0: 
        for i in range(4,Length_1):
            element = Lesson_list_1[i]
            List_1 = Lesson_list_1[i].text # текст Урок № и название
            New_list_1 = List_1.split()  # разбили на списки, разделив каждое слово
            if New_list_1[0] == 'УРОК':
                New_list_1.pop(0) #удалили первое слово из списка "Урок"
                New_list_1.pop(0) #удалили второе слово из списка № Урока
                List_of_lesson_title_1 = ' '.join(New_list_1) #объединили слова из названия урока в список из названия уроков 
                if List_of_lesson_title_1 == Lesson:
                    element.click()
                    lesson_title_1 = driver.find_elements_by_tag_name('h3')[0] # название урока в уроке
                    Text_lesson_title_1 = lesson_title_1.text
                    if len(Text_lesson_title_1)!= 0: 
                        if Text_lesson_title_1 == Lesson:
                            link_name = driver.find_element_by_tag_name('iframe').get_attribute("src") # ссылка на видеоурок
                            driver.get(link_name) # запуск видео урока в новом окне
                            title_video_lesson = driver.find_element_by_class_name('ytp-title-text')# надпись "название урока| предмет"
                            title_video_lesson_text = title_video_lesson.text # текст "название урока| предмет"
                            video_lesson_title = title_video_lesson_text.split('|')
                            video_lesson_title_1 = video_lesson_title [0].strip(' ')
                            video_lesson_subject = video_lesson_title [-1].strip(' ')
                            first_word_video_lesson_subject = video_lesson_subject.split()
                            print ('РЕЗУЛЬТАТ:')
                            if video_lesson_title_1 == Lesson and (first_word_video_lesson_subject[0] == item_name or first_word_video_lesson_subject[0] == 'Беларуская'):  # Lesson - это название урока из списка уроков, который появляется после выбора предмета
                                return 'Название урока из списка уроков совпадает с названием урока в самом уроке\n'+'Название видеоурока совпадает с названием урока\n'+'Предмет видеоурока совпадает с предметом'
                            elif video_lesson_title_1 == Lesson and first_word_video_lesson_subject[0] != item_name:
                                return 'Название урока из списка уроков совпадает с названием урока в самом уроке\n'+'Название видеоурока совпадает с названием урока\n'+'Предмет видеоурока НЕ совпадает с предметом'
                            elif video_lesson_title_1 != Lesson and first_word_video_lesson_subject[0] == item_name:
                                return 'Название урока из списка уроков совпадает с названием урока в самом уроке\n'+'Название видеоурока НЕ совпадает с названием урока\n'+'Название видео урока: '+video_lesson_title_1,'\n'+'Предмет видеоурока совпадает с предметом'
                            elif video_lesson_title_1 != Lesson and first_word_video_lesson_subject[0] == item_name:
                                return 'Название урока из списка уроков совпадает с названием урока в самом уроке\n'+'Название видеоурока НЕ совпадает с названием урока в самом уроке\n'+'Название видео урока: '+video_lesson_title_1,'\n'+'Предмет видеоурока совпадает с предметом'
                        else:
                            return 'Название урока из списка уроков НЕ СОВПАДАЕТ с названием урока в самом уроке!'
                    else:
                        return f'Урок "{Lesson}" в разработке'
            else:
                return f'работа {New_list_1[0]}А проверяется отдельно'




random_subject = Subject_selection()
text_item_name = random_subject.text
first_word_text_item_name = text_item_name.split() 
first_word_name_subject = first_word_text_item_name[0]
print (text_item_name) # печатает название предмета
random_subject.click()	# нажимает на предмет


Button_lesson_number  = driver.find_elements_by_class_name('subject-number') #кнопка "УРОК N"
if len(Button_lesson_number) != 0:
    random_lesson_title = Lesson_selection() # выбор случайного урока
    print('Урок:',random_lesson_title)  # печать выбранного урока
    result = Lesson_title(random_lesson_title, first_word_name_subject)
    print (result)
else:
    print ('Предмет "'+text_item_name+'" в разработке')	
#









# The End
