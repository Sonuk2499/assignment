import requests as req
from bs4 import BeautifulSoup
url="https://www.worldometers.info/coronavirus/"
page=req.get(url)
#htmlContent=r.content
#print(htmlContent)
print(page.status_code)

soup= BeautifulSoup(page.text,'html.parser')
Worldmeter=soup.find('Worldmeter',class_="navbar-brand")
print(Worldmeter)
headers = []
first_row=Worldmeter.find('tr')

for i in first_row.find_all('th'):
 title = i.text
 headers.append(title)

print(headers)