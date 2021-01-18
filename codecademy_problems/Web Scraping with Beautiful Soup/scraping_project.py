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
# print(ratings)
# plt.hist(ratings)
# plt.show()

all_company_tag = soup.select(".Company")
# print(all_company_tag)

companies = []

for tag in all_company_tag[1:]:
  companies.append(tag.get_text())

# print(companies)

d = {"Company Name": companies, "Rating": ratings}
chdf = pd.DataFrame.from_dict(d)

# print(chdf.head(10))

mean_vals = chdf.groupby("Company Name").Rating.mean()
# print(mean_vals.head(10))
ten_best = mean_vals.nlargest(10)
print(ten_best)
