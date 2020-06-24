import requests
from pprint import pprint
#city= input('enter your city name: ')
city= 'Lahore'

# get api  key from https://home.openweathermap.org/api_keys
# assign above key to appid= , at end of url 
# c73ac6efebc7530e7ecd1b201e657372 is my  API key

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=c73ac6efebc7530e7ecd1b201e657372&units=metric'.format(city)
     
res= requests.get(url)

Data= res.json()
#pprint(res.json())

Temp= Data['main']['temp']
wind_speed= Data['wind']['speed']
latitude = Data['coord']['lat']
longitude= Data['coord']['lon']

print( 'Temp:{}'.format(Temp))
print( 'Wind_speed:{}'.format(wind_speed))
print( 'Latitude:{}'.format(latitude))
print( 'Longitude:{}'.format(longitude))