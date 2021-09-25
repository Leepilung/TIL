# 
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle


url = 'https://platum.kr/archives/120958'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

print("og_image : ",og_image)
print("og_title : ",og_title) # <meta content="[Startup’s Story #449] 중국서 공유주택 열기 일으킨 창업가, 한국서 이어간다" property="og:title"/> 출력
print("og_title['content'] : ",og_title['content']) #  [Startup’s Story #449] 중국서 공유주택 열기 일으킨 창업가, 한국서 이어간다 출력
print("og_description : ",og_description)

url_image = og_image['content']
url_title = og_title['content']
url_description = og_description['content']

print("url_image : ",url_image)
print("url_title : ",url_title)
print("url_description : ",url_description)

doc = { 'image' : url_image, 'title' : url_title, "description" : url_description }

all_doc = list(db.article.find({}))
print(all_doc)
