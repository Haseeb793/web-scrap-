from selenium import webdriver 

from bs4 import BeautifulSoup
import requests


driver= webdriver.Chrome()


#driver= webdriver.Chrome(r"C:\Users\Mannan\Downloads\Programs\chromedriver.exe")

driver.get('https://www.hackerearth.com/challenges/')
res= driver.execute_script( 'return document.documentElement.outerHTML')
driver.quit()


soup= BeautifulSoup(res, 'lxml')
challange_type= soup.find('div',class_="ongoing challenge-list" ).find_all(class_="challenge-card-modern")[0].find(class_="challenge-type")
challange_name= soup.find('div',class_="ongoing challenge-list" ).find_all(class_="challenge-card-modern")[0].find(class_="challenge-name").text
challange_date= soup.find('div',class_="ongoing challenge-list" ).find_all(class_="challenge-card-modern")[0].find(class_="date").text.replace('\n','').strip()




print(challange_date)