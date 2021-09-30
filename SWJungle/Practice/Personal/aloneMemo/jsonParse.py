from bs4 import BeautifulSoup
from flask.json import JSONEncoder
from bson import ObjectId
import requests
from werkzeug.routing import BaseConverter



# Json파일 Encoing -> ObjectId값만 문자열(str)으로 변환
class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)

# ObjectId 파싱용 
class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)


# 웹스크리핑용 헤더
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 데이터 parsing
def createMemoEntity(url, comment):
    parsed = parseUrlMetaData(url)
    return {'url': url, 'title': parsed['title'], 'desc': parsed['description'], 'image': parsed['image'],
            'comment': comment}

# 데이터 스크래핑 -> json 형태로 createMemoEntity에 전달
def parseUrlMetaData(url):
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_title = og_title['content'] if og_title else 'title이 존재하지 않습니다.'
    url_description = og_description['content'] if og_description else 'description이 존재하지 않습니다'
    url_image = og_image['content'] if og_image else 'image가 존재하지 않습니다.'

    return {'title': url_title, 'description': url_description, 'image': url_image}
    
