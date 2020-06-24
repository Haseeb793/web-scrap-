import requests
from pprint import pprint
import re

def by_loccation ():

    # this block of code to get lat and long from ip address
    res= requests.get('https://ipinfo.io/')
    Data= res.json()   # json is similar to python dictionary

    lat= Data['loc'].split(',')[0]
    lon= Data['loc'].split(',')[1]

    # get api  key from https://home.openweathermap.org/api_keys
    # c73ac6efebc7530e7ecd1b201e657372 is my  API key
    # assign above key to appid= , at end of url 

    #api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your api key}
    #http://api.openweathermap.org/data/2.5/weather?lat=33.55&lon=74.34&appid=c73ac6efebc7530e7ecd1b201e657372
    url= 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=c73ac6efebc7530e7ecd1b201e657372'.format(lat,lon)

    res= requests.get(url)


    Data= res.json()
    #pprint(res.json())
    show_data(Data)






def show_data(Data) : #data in jason format

    Temp= Data['main']['temp']
    wind_speed= Data['wind']['speed']
    latitude = Data['coord']['lat']
    longitude= Data['coord']['lon']

    print( 'Temp:{} kelvin'.format(Temp))
    print( 'Wind_speed:{} m/s'.format(wind_speed))
    print( 'Latitude:{}'.format(latitude))
    print( 'Longitude:{}'.format(longitude))

def main():
    by_loccation ()



if __name__ == "__main__":
    main()