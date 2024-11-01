import requests
import json
from bs4 import BeautifulSoup

def pasres(page):
    url = f'https://quotes.toscrape.com/{page}/'
    query = requests.get(url)
    soup = BeautifulSoup(query.content, "html.parser").text
    return soup

page=''
result=pasres(page)
with open('Result.json', 'w') as file:
    json.dump(result, file)







