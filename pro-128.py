from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
headers = ["Name", "Distance", "Mass", "Radius"]
dwarf_data = []
temp_list = []
def scrape():
    try:
        page = requests.get(START_URL)
        soup = BeautifulSoup(page.content,"html.parser")
        
        star_table = soup.find_all('table') 
        temp_list= [] 
        table_rows = star_table.find_all('tr') 
        for tr in table_rows: 
            td = tr.find_all('td') 
        row = [i.text.rstrip() for i in td] 
        temp_list.append(row)
        
    except:
        time.sleep(1)
        scrape()

scrape()

Dwarf_names = [] 
Distance =[] 
Mass = [] 
Radius =[]  
print(len(temp_list))
for i in range(1,len(temp_list)): 
    Dwarf_names.append(temp_list[i][0]) 
    Distance.append(temp_list[i][5]) 
    Mass.append(temp_list[i][7]) 
    Radius.append(temp_list[i][8]) 

df2 = pd.DataFrame(list(zip(Dwarf_names,Distance,Mass,Radius)),columns=['Name','Distance','Mass','Radius']) 
print(df2) 
df2.to_csv('dwarfs.csv')