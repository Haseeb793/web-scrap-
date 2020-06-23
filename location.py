from bs4 import BeautifulSoup
import requests
import re

res= requests.get('https://ipinfo.io/')
Data= res.json()   # json is similar to python dictionary
print( 'city: {}'.format(Data['city']) )
print( 'longitude:' + Data['loc'].split(',')[0] ) 
print( 'longitude:' + Data['loc'].split(',')[1] ) 

