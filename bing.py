from bs4 import BeautifulSoup
import requests
import urllib.request

res= requests.get('https://bing.wallpaper.pics/')
soup= BeautifulSoup(res.text, 'lxml')
imageUrl= soup.find('div', class_='panel').find('img')['src']

urllib.request.urlretrieve(imageUrl , 'bing.jpg')