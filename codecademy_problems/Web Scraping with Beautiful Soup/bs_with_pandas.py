import requests
from bs4 import BeautifulSoup
import pandas as pd

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []

for a in turtle_links:
  links.append(prefix+a["href"])

turtle_data = {}

for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()

  stats = turtle.find("ul")
  stats_text = stats.get_text("|").split("|")
  di = []
  for data in stats_text:
      if data != '\n':
          di.append(data.strip())

  turtle_data[turtle_name] = di


turtle_df = pd.DataFrame.from_dict(turtle_data, orient='index')

# print(turtle_df.head(10))
turtle_df = turtle_df.reset_index()
turtle_df.columns = ['name', 'age','weight_lbs','sex','breed','source']


turtle_df['age'] = turtle_df['age'].str.extract('(\d+)').apply(pd.to_numeric)
turtle_df['weight_lbs'] = turtle_df['weight_lbs'].str.extract('(\d+)').apply(pd.to_numeric)

turtle_df['sex'] = turtle_df['sex'].str.split().str[-1]
turtle_df['breed'] = turtle_df['breed'].str.split(':').str[-1]
turtle_df['source'] = turtle_df['source'].str.split(':').str[-1]

print(turtle_df.head())
