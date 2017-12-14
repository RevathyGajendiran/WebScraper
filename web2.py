#Accessing the table header of the table in the webpage.
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='https://en.wikipedia.org/wiki/List_of_districts_in_Tamil_Nadu'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
name_box = page_soup.find('table', class_='wikitable sortable')
city=name_box.tr
city2=city.text
print(city2)
