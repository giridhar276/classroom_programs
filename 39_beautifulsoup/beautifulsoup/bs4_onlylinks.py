from bs4 import BeautifulSoup

import requests


r  = requests.get("http://google.com")

data = r.text

soup = BeautifulSoup(data,'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
