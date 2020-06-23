from bs4 import BeautifulSoup
from urllib.request import urlopen 
import pandas as pd 

html= urlopen("https://www.psx.com.pk/")

contents= html.read()

# empty list 
data = [] 
   
# for getting the header 
list_header = [] 

soup = BeautifulSoup( contents ,'html.parser')
header = soup.find_all(class_="market-overview")[0].find("tr") 

for items in header: 
    try: 
        list_header.append(items.get_text()) 
    except: 
        continue
print(list_header)

# for getting the data  
HTML_data = soup.find_all(class_="market-overview")[0].find_all("tr")[1:] 

for element in HTML_data: 
    sub_data = [] 
    for sub_element in element: 
        try: 
            sub_data.append(sub_element.get_text()) 
        except: 
            continue
    data.append(sub_data)    
print(data)

# Storing the data into Pandas 
# DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header) 


# Converting Pandas DataFrame 
# into CSV file 
dataFrame.to_csv('Market_Summary.csv') 


