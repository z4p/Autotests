from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from random import choice

driver = webdriver.Chrome("C:\\Alla_work\\chromedriver.exe")
driver.get("https://adukar.by/")
wait = WebDriverWait(driver,200)


Search_queries_march_2020 = [
'куда поступать на экономиста',
'где учат на экономиста',
'поступить в вуз польши',
'ВУЗы Польши',
'проходные баллы на экономиста',
'конкурс на экономиста',
'бюджет на экономиста',
'льготы при поступлении',
'проходные баллы',
'даты цт 2020',
'пороговые баллы цт',
'регистрация на цт',
'поступить без цт',
'высокооплачиваемая профессия',
'как войти в it',
'как стать BA специалистом',
'лучшие университеты',
'лучшие вузы'
]



def Search_query_march_2020():
    return choice(Search_queries_march_2020) #возвращение случайного запроса из списка
  
Query = Search_query_march_2020()


element = driver.find_elements_by_class_name('icon-label')[0] #кнопка поиск
element.click()
element = driver.find_element_by_class_name('ui-autocomplete-input')#кнопка для ввода текста в поиск
element.send_keys(Query)
element.send_keys(Keys.RETURN)	
print ('РЕЗУЛЬТАТЫ ПОИСКА: * отображается текст: Результаты поиска по запросу «'+Query+'»')
print ('                   * возможно наличие кнопки "Высшие учебные заведения"')
print('                      - ВУЗы содержат информацию по запросу:',Query)
print ('                     - количество ВУЗов соответвует счетчику на кнопке "Высшие учебные заведения"')
print ('                   * возможно наличие кнопки "Колледжи и профессиональные лицеи":')
print('                      - колледжи и профессиональные лицеи содержат информацию по запросу:',Query)
print('                      - количество колледжей и профессиональных лицеев соответвует счетчику на кнопке "Колледжи и профессиональные лицеи"')
print ('                   * кнопка "Новости":')
print('                      - новости связаны с запросом:',Query)
print('                      - количество новостей соответвует счетчику на кнопке "Новости"')
print('                    * По запросу «'+Query +'» ничего не найдено')

	
assert "Страница не найдена" not in driver.page_source