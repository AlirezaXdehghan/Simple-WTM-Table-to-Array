import requests
from bs4 import BeautifulSoup
page = requests.get("https://whattomine.com/")
soup = BeautifulSoup(page.content,'html.parser')
fulltable = soup.find("table", { "class" : "table table-sm table-hover table-vcenter" })
rows = fulltable.findAll("tr")
tableMatrix=[]
for i in range(len(rows)):
    tableMatrix.append(rows[i].findAll("td"))
tableMatrix.remove([])
print(tableMatrix)
