import codecademylib3_seaborn
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

# print(webpage.content)

soup = bs(webpage.content, "html.parser")
# print(soup)

rating_tag = soup.find_all(attrs={"class": "Rating"})
# print(rating_tag)

ratings = []

for tag in rating_tag[1:]:
  ratings.append(float(tag.get_text()))

plt.hist(ratings)
plt.show()
