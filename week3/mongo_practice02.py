from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

#(1) 영화 제목 월-e 의 평점 가져오기
target_movies = db.movies.find_one({'title': '월-E'})
#평점만 꺼내오기
print(target_movies['star'])
#========================================================

#(2) 월-e의 평점과 같은 평점의 영화 제목들을 가져오기
target_movies = db.movies.find_one({'title': '월-E'})
#평점만 꺼내오기
target_star = target_movies['star']
target_movies2 = db.movies.find({'star' : target_star})

for movie in target_movies2:
    print(movie['title'])

#=========================================================

