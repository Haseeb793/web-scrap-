from bs4 import BeautifulSoup
import requests

res= requests.get('https://www.goodreads.com/quotes/tag/web-development')
#print(res)
#print(res.text)

soup= BeautifulSoup(res.text, 'lxml')  # soup is document type object 
list_of_Quote= soup.find_all('div',class_="quoteText")

'''
method 1
for numb in range(int(len(list_of_Quote)) ):

     print(list_of_Quote[numb].get_text())
'''

#method 2
for q in list_of_Quote:

     print(q.get_text())


#get author names
#authorOrTitle= first_Quote= soup.find_all(class_="quoteText")[2].find(class_="authorOrTitle")
#print(authorOrTitle.get_text())