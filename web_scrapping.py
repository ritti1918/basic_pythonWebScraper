'''Pick a website and describe your objective
1.Browse through different sites and pick on to scrape.
2.List the infos to be scraped from the site.
3.Summarize the project.'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook
url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets' 
response=requests.get(url)
#print(response)
s=BeautifulSoup(response.text,'lxml')
# print(s)

names=s.find_all('a',class_='title')
list1=[i.text for i in names]
# print(list1)

prices=s.find_all('h4',class_='pull-right price')
list2=[i.text for i in prices]
# print(list2)

descrip=s.find_all('p',class_='description')
list3=[i.text for i in descrip]
# print(list3)
   
df=pd.DataFrame({'Brand_name':(list1),
                  'Price'     :(list2),
                  'Description':(list3),
                  })
# print(df)

df.to_excel('dataextract.xlsx',index=False)
