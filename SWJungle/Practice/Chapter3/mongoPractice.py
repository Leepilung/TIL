from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
print(db)
# 코딩 시작

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})

# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({}))

# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
same_ages = list(db.users.find({'age':21}))

print(all_users[0])         # 0번째 결과값을 보기
print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
    print(user)

user = db.users.find_one({'name':'bobby'})
print('user 1 : ',user)

# 그 중 특정 키(id) 값을 빼고 보기
user = db.users.find_one({'name':'bobby'},{'_id':False})
print('user 2 : ',user)

# 수정하기

# 생김새
# db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })

# 예시 - 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'}) # bobby라는 name값을 가진 값의 age값이 21 -> 19로 바뀜.
print(user)

# 삭제하기(거의 안 씀)
db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})  
print(user) # -> 삭제되서 찾을 수없으면 none 출력됨.