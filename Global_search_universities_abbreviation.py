from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from random import choice

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,200)

Universities_abbreviation = [
'АУпПРБ', 'БГМУ', 'БГПУ имени Максима Танка', 'Белорусский государственный университет', 'БГУИР', 'БГЭУ',
'БНТУ', 'БрГУ имени А. С. Пушкина', 'ВГАВМ', 'ВГУ имени П. М. Машерова', 'ГГУ имени Франциска Скорины',
'ГрГУ имени Янки Купалы', 'Академия МВД РБ', 'БарГУ', 'БГАА', 'БГАИ', 'БГАМ', 'БГАС', 'БГАС. Витебский филиал',
'БГСХА', 'БГАТУ', 'БГТУ', 'БГУКИ', 'БелГУТ', 'БГУФК', 'БТЭУ', 'БРУ', 'БГУ', 'БИП', 'БрГТУ', 'ВПУ', 'ВУ', 'ВГМУ',
'ВГТУ', 'ВА РБ', 'ВТУ', 'ВУ', 'ГМУ', 'ГПУ', 'ГГМУ', 'ГГТУ имени П. О. Сухого', 'ГГАУ', 'ГрГМУ', 'ЕГУ', 'ИПП', 
'ИПС РБ', 'ИПД', 'ИСЗ имени А. М. Широкова', 'МФТИ', 'НИУ ВШЭ', 'ПолесГУ', 'ПГУ', 'РГСУ. Минский филиал', 
'РЭУ имени Г. В. Плеханова. Минский филиал', 'СПбГУ', 'УГЗ МЧС РБ', 'ПУ имени Адама Мицкевича', 'УМКС', 'ЧИУП', 'ЯУ'
]

element = driver.find_elements_by_class_name('icon-label')[0] #кнопка поиск
element.click()
element = driver.find_element_by_class_name('ui-autocomplete-input')#кнопка для ввода текста в поиск
 
def find_universities_abbreviation():
    return choice(Universities_abbreviation)
    
university = find_universities_abbreviation()
print ('Университет:',university)
element.send_keys(university)
element.send_keys(Keys.RETURN)	
	
assert "Страница не найдена" not in driver.page_source
