from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

stars_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(stars_url)
print(page)
soup=bs(page.text,"html.parser")
star_table=soup.find("table")

temp_list=[]
table_rows=star_table.find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

str_names=[]
distance=[]
mass=[]
radious=[]
lum=[]

for i in range(1,len(temp_list)):
    str_names.append(temp_list[i][1])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][6])
    radious.append(temp_list[i][8])
    lum.append(temp_list[i][9])

df=pd.DataFrame(list(zip(str_names,
distance,
mass,
radious,
lum,)),columns=["star_name","distance","mass","radius","luminosity"])
print(df)
df.to_csv("bright_stars.csv")