from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_serach_results_df(keyword):
  columns = ['rank', 'title', 'url', 'affiliate_url']
  df = pd.DataFrame(columns=columns)
  html_doc = requests.get('https://www.google.co.jp/search?num=10&q=' +keyword).text
  soup = BeautifulSoup(html_doc, 'html.parser')
  tags =soup.find_all('h3',{'class':'r'})
  rank=1
  for tag in tags:
    title = tag.text
    url = query_string_remove(tag.select("a")[0].get("href").replace("/url?q=",""))
    affiliate_url = ""
    se = pd.Series([rank,title, url, affiliate_url], columns)
    df = df.append(se, ignore_index=True)
    rank += 1
  return df

def query_string_remove(url):
  return url[:url.find('&')]

keyword = ""
search_results_df = get_serach_results_df(keyword)
search_results_df.head(10)
print(search_results_df.head(10))

def get_a8_links(url):
  html_doc = requests.get(url).text
  soup = BeautifulSoup(html_doc, 'html.parser')
  tags = soup.select("a")
  urls = ""
  for tag in tags:
    url = tag.get("href")
    if url.find("https://px.a8.net/") > 1 :
      urls += url + "\n"
  return urls
    
url = "https://dividable.net/programming-school/recommended-programming-school"
print(get_a8_links(url))
      