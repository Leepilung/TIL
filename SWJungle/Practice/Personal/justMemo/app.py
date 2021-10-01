from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

# ObjectId Json 파싱
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
# ObjectId -> Json파싱
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

# MongoDB 연결
client = MongoClient('localhost',27017)
db = client.Practice  # Practice db 사용.

# 홈페이지 라우팅
@app.route('/')
def home():
    return render_template('index.html')

# get 라우트 전체출력
@app.route('/memos', methods=['GET'])
def get():
    records = db.memos.find()

    return jsonify({'memos': list(records)})

# get 라우트 특정 id값만 출력
@app.route('/memos/<objectid:id>', methods=['GET'])
def getOne(id):
    record = db.memos.find_one({'_id': id})

    return jsonify({'memo' : record})

# post 메소드
@app.route('/memos', methods=['POST'])
def post():
    title = request.json.get('title')
    body = request.json.get('body')

    db.memos.insert_one({'title':title,'body':body})

    return jsonify({'result' : 'post success'})

# PUT 메소드
@app.route('/memos/<objectid:id>', methods=['PUT'])
def put(id):
    title = request.json.get('title')
    body = request.json.get('body')

    db.memos.update_one({'_id':id}, {'$set' : {'title' : title, 'body' : body}})

    return jsonify({'status' : 'update success'})

# DELETE 메소드
@app.route('/memos/<objectid:id>', methods=['DELETE'])
def delete(id):
    db.memos.delete_one({'_id':id})

    return {'status' : 'delete success'}

if __name__ == '__main__':
    app.run('0.0.0.0', port=2222, debug=True)