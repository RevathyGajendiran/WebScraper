#extracting the district table into excel
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd 
import xlrd
my_url='https://en.wikipedia.org/wiki/List_of_districts_in_Tamil_Nadu'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
#city_tables = page_soup.find_all('table', class_='wikitable sortable')
#name = name_box.text.strip() # strip() is used to remove starting and trailing
#for i in range(1,10):
pd.set_option('max_columns', 9)
citydetails = pd.read_html(my_url)[2]
citydetails.to_excel('citydetails.xlsx', index=False)
