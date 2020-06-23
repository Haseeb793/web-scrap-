from bs4 import BeautifulSoup
import requests

res= requests.get('https://www.brainyquote.com/quote_of_the_day')
soup = BeautifulSoup(res.text,'lxml')
Quote = soup.find('img', id="qimage_100748")
print(Quote['alt'])
