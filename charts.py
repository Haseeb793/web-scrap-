from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.jiosaavn.com/featured/weekly-top-songs/8MT-LQlP35c_')
soup = BeautifulSoup(res.text ,'lxml')
data= soup.find('ol',class_="o-list-bare u-margin-bottom-none@sm")


song_headers= data.find_all('h4', "u-centi u-ellipsis u-color-js-gray u-margin-bottom-none@sm")

for song in song_headers:
    song_name=song.find('a')
    print(song.text)


