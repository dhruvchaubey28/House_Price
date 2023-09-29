import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=New-Delhi&BudgetMin=50-Lacs")

soup=BeautifulSoup(req.content,"html.parser")
print(soup.get_text())
print(soup.prettify())

