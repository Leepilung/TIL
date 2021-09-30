from bson import ObjectId
# utils 파일 불러오는 부분
from jsonParse import MongoJSONEncoder, ObjectIdConverter, createMemoEntity, parseUrlMetaData

from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)


app = Flask(__name__)
# ObjectId -> Json파싱
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

# client = MongoClient('mongodb://설정한아이디:비밀번호@내AWS아이피',27017) 와 같은 뜻
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.alonememo  # 'alonememo'라는 이름의 db를 만들어서 사용.

# 홈페이지 라우팅
@app.route('/')
def home():
    return render_template('index.html')

# 전체 출력 get 메소드(Read)
@app.route('/memos', methods=['GET'])
def getMemos():
    result = db.articles.find()
    return jsonify({'memos': list(result)})

# 특정 id값만 get 메소드(Read)
@app.route('/memos/<objectid:id>', methods=['GET'])
def getMemo(id):
    result = db.articles.find_one({'_id': id})
    return jsonify({'memo': result})

# post 메소드(Create)
@app.route('/memos', methods=['POST'])
def postMemo():
    #  클라이언트로부터 데이터 받는부분
    url = request.json['url']  # 클라이언트로부터 url을 받는 부분
    comment = request.json['comment']  # 클라이언트로부터 comment를 받는 부분

    article = createMemoEntity(url, comment)

    db.articles.insert_one(article)

    return jsonify({'result': 'success'})

# PUT 메소드(Update)
@app.route('/memos/<objectid:id>', methods=['PUT'])
def putMemo(id):
    url = request.json['url']  # 클라이언트로부터 url을 받는 부분
    comment = request.json['comment']  # 클라이언트로부터 comment를 받는 부분

    article = createMemoEntity(url, comment)

    db.articles.update_one({'_id': id}, {'$set': article})

    return jsonify({'status': 'success'})

# Delete 메소드(Delete)
@app.route('/memos/<objectid:id>', methods=['DELETE'])
def deleteMemo(id):
    db.articles.delete_one({'_id': id})
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
