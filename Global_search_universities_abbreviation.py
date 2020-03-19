from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from random import choice

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,200)

Universities_abbreviation_march_2020 = [
'АУпПРБ', 'БГМУ', 'БГПУ имени Максима Танка', 'Белорусский государственный университет', 'БГУИР', 'БГЭУ',
'БНТУ', 'БрГУ имени А. С. Пушкина', 'ВГАВМ', 'ВГУ имени П. М. Машерова', 'ГГУ имени Франциска Скорины',
'ГрГУ имени Янки Купалы', 'Академия МВД РБ', 'БарГУ', 'БГАА', 'БГАИ', 'БГАМ', 'БГАС', 'БГАС. Витебский филиал',
'БГСХА', 'БГАТУ', 'БГТУ', 'БГУКИ', 'БелГУТ', 'БГУФК', 'БТЭУ', 'БРУ', 'БГУ', 'БИП', 'БрГТУ', 'ВПУ', 'ВУ', 'ВГМУ',
'ВГТУ', 'ВА РБ', 'ВТУ', 'ВУ', 'ГМУ', 'ГПУ', 'ГГМУ', 'ГГТУ имени П. О. Сухого', 'ГГАУ', 'ГрГМУ', 'ЕГУ', 'ИПП', 
'ИПС РБ', 'ИПД', 'ИСЗ имени А. М. Широкова', 'МФТИ', 'НИУ ВШЭ', 'ПолесГУ', 'ПГУ', 'РГСУ. Минский филиал', 
'РЭУ имени Г. В. Плеханова. Минский филиал', 'СПбГУ', 'УГЗ МЧС РБ', 'ПУ имени Адама Мицкевича', 'УМКС', 'ЧИУП', 'ЯУ'
]

def find_universities():
    return choice(Universities_abbreviation_march_2020) #возвращение случайного ВУЗа из списка
  
University = find_universities()


element = driver.find_elements_by_class_name('icon-label')[0] #кнопка поиск
element.click()
element = driver.find_element_by_class_name('ui-autocomplete-input')#кнопка для ввода текста в поиск
element.send_keys(University)
element.send_keys(Keys.RETURN)	
print ('РЕЗУЛЬТАТЫ ПОИСКА: * отображается кнока "Высшие учебные заведения"')
print ('                   * отображается ВУЗ:',University)
print ('                   * количество ВУЗов соответвует счетчику на кнопке "Высшие учебные заведения"')
print ('                   * возможно наличие кнопки "Колледжи и профессиональные лицеи":')
print('                      - колледжи и профессиональные лицеи являются филиалами ВУЗа:',University)
print('                      - количество колледжей и профессиональных лицеев соответвует счетчику на кнопке "Колледжи и профессиональные лицеи"')
print ('                   * возможно наличие кнопки "Новости":')
print('                      - новости связаны с ВУЗом',University)
print('                      - количество новостей соответвует счетчику на кнопке "Новости"')

	
assert "Страница не найдена" not in driver.page_source
