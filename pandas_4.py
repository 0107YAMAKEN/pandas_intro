from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_search_results_df(keyword):
 columns = ['rank','title','url', 'affiliate_url']
 df = pd.DataFrame(columns=columns)
 html_doc = requests.get('https://www.google.co.jp/search?num=10&q=' +keyword).text
 soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
 tags = soup.find_all('h3',{'class':'r'})
 rank = 1
 for tag in tags:
   title = tag.text
   url = query_string_remove(tag.select("a")[0].get("href").replace("/url?q=",""))
   affiliate_url = ""
   se = pd.Series([rank, title, url, affiliate_url], columns)
   df = df.append(se, ignore_index=True)
   rank += 1
 return df
 
def query_string_remove(url):
 return url[:url.find('&')]

def get_a8_links(url):
 html_doc = requests.get(url).text
 soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
 tags = soup.select("a")
 urls = ""
 for tag in tags:
   url = tag.get("href")
   if url.find(a8_link) > -1 :
     urls += url + "\n"
 return urls