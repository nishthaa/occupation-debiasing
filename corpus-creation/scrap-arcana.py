from bs4 import BeautifulSoup

import requests

fhandle = open("arcana-occupations.txt","a")

r=requests.get("http://arcana.wikidot.com/list-of-all-occupations")
data=r.text

soup = BeautifulSoup(data, "html.parser")

for item in soup.find_all("a",href = True, class_="newpage"):

    occupation = (str(item['href']).lstrip("/"))+"\n"
    
    fhandle.write(occupation)
