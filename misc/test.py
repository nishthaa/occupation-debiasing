from bs4 import BeautifulSoup
import requests


r=requests.get("https://en.wikipedia.org/wiki/Category:Occupations")
data=r.text

soup = BeautifulSoup(data, "html.parser")

sub_headings = soup.find_all("h2")
print(sub_headings)

container_div = soup.find_all(class_="mw-category-group")


ulist = container_div[1]
print(ulist.ul.li)



