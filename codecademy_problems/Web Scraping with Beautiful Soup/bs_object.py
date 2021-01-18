import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html', 'html.parser')

webpage = webpage_response.content

soup = BeautifulSoup(webpage)

print(soup)
