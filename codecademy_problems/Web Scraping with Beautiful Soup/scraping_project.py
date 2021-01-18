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
# print(ten_best)

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")

for td in cocoa_percent_tags[1:]:
  percent = float(td.get_text().strip('%'))
  cocoa_percents.append(percent)

chdf['CocoaPercentage'] = cocoa_percents

# print(chdf.head(10))

plt.scatter(chdf.CocoaPercentage, chdf.Rating)
plt.show()


z = np.polyfit(chdf.CocoaPercentage, chdf.Rating, 1)
line_function = np.poly1d(z)
plt.plot(chdf.CocoaPercentage, line_function(chdf.CocoaPercentage), "r--")

plt.show()
