import requests
from bs4 import BeautifulSoup

URL = 'https://www.monex.com/silver-prices/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='priceTBL').getText()
prices = soup.find(id='spotoz').getText()

print(results, prices)



