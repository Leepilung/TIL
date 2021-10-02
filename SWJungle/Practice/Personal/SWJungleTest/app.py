# SW사관학교 정글 입학시험 app.py 파일 // 이필웅 개인식별번호 : LDJTBQRDSX 
# Flask, Pymongo 패키지
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient 

# ObjectId Json 파싱용 
from bson import ObjectId
from flask.json import JSONEncoder
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

app = Flask(__name__)
# ObjectId -> Json으로 파싱하기 위한 구문
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

# MongoDB 연결 //
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.JustMemo 

# API Restful하게 짜기(restx or restful 사용X)
@app.route('/')
def home():
    return render_template('index.html')

# get 라우트 전체출력
@app.route('/memos', methods=['GET'])
def get():
    memos = db.memos.find()

    return jsonify({'memos': list(memos)})

# GET 라우트 특정 id값만 출력
@app.route('/memos/<objectid:id>', methods=['GET'])
def getOne(id):
    memo = db.memos.find_one({'_id': id})

    return jsonify({'memo' : memo})

# POST 메소드
@app.route('/memos', methods=['POST'])
def post():
    title = request.json.get('title')
    body = request.json.get('body')

    db.memos.insert_one({'title':title,'body':body})

    return jsonify({'result' : 'POST success'})

# PUT 메소드
@app.route('/memos/<objectid:id>', methods=['PUT'])
def put(id):
    title = request.json.get('title')
    body = request.json.get('body')

    db.memos.update_one({'_id':id}, {'$set' : {'title' : title, 'body' : body}})

    return jsonify({'status' : 'UPDATE success'})

# DELETE 메소드
@app.route('/memos/<objectid:id>', methods=['DELETE'])
def delete(id):
    db.memos.delete_one({'_id':id})

    return {'status' : 'DELETE success'}

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)