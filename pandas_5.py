#find関数でa8ネットのアフィリエイトリンクを自動生成できる関数を作成
from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_a8_links(url):
  html_doc = requests.get(url).text
  soup = BeautifulSoup(html_doc,'html.parser')
  tags = soup.select("a")
  urls = ""
  for tag in tags:
    url = tag.get("href")
    if url.find("https://px.a8.net/") > -1 :
      urls += url + "\n"
  return urls
  
  
url = "https://dividable.net/programming-school/recommended-programming-school"
print(get_a8_links(url))
  
    