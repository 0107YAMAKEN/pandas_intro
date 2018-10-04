import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://review-of-my-life.blogspot.com"

response = requests.get(url).text
#print(response)

soup = BeautifulSoup(response, 'html.parser')
#print(soup.prettify())

tags = soup.find_all("h3",{"class":"post-title"})
#print(tags)

columns = ["name", "url"]
df2 = pd.DataFrame(columns=columns)


for tag in tags:
 name = tag.a.string
 url = tag.a.get("href")
 se = pd.Series([name, url], columns)
 print(se)
 df2 = df2.append(se, columns)


filename = "result.csv"
df2.to_csv(filename, encoding = 'utf-8')
