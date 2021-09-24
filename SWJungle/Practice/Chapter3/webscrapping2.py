from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

# 예제 1. DB에서 매트릭스 평점찾기.

# 고찰해봐야할 부분 -> 컬렉션 명을 잘못입력함. 찾을떄에는 db.컬렉션명
# 또한 그냥 matrix_rank만 찾으면 해당 다큐먼트의 모든값을 출력해버림.
# 거기서 따로 원하는 값이 있으면 인덱스를
# 찾는것처럼(혹은 딕셔너리에서 값찾기) ['찾으려는값']을 붙여야함.

matrix_rank = db.movies.find_one({'title':'매트릭스'})

print(matrix_rank['star'])

# 예제 2. '매트릭스'와 평점이 같은 평점의 영화 제목들 가져오기

same_star = list(db.movies.find({'star':"9.39"}))

for movie in same_star:
    print(movie['title'])

# 예제 3. 매트릭스 영화의 평점 0으로 만들어보기.

db.movies.update_one({'title':'매트릭스'},{'$set' : {'star':0}})

print(db.movies.find_one({'title':'매트릭스'})['star'])