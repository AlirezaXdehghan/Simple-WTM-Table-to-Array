import requests
from bs4 import BeautifulSoup
page = requests.get("https://whattomine.com/")
soup = BeautifulSoup(page.content,'html.parser')
fulltable = soup.find("table", { "class" : "table table-sm table-hover table-vcenter" })
rows = fulltable.findAll("tr")
tableMatrix=[]
NamePriceMatrix=[]
for i in range(len(rows)):
    tableMatrix.append(rows[i].findAll("td"))
tableMatrix.remove([])

#remove the unnecessary entries that come with the td tag
j=0
while j<len(tableMatrix):
    if (tableMatrix[j][0].text.find('(') == -1):
        tableMatrix.remove(tableMatrix[j])
    else:
        j=j+1

#get the raw price and names and put them in a new matrix
for i in range (len(tableMatrix)):
    first = tableMatrix[i][7].text.find('$')+1
    last = tableMatrix[i][7].text.find('$', first+1)
    String = tableMatrix[i][7].text[first:last]
    Price = float(String)
    Name = tableMatrix[i][0].text.strip()
    NamePriceMatrix.append([Name, Price])

print(NamePriceMatrix)
