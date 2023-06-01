import json
import requests

TMDB_API_KEY = '4989c16e3df7b1d6ddefb4043cea3793'


def get_movie_data():
	result_data = []

	for i in range(1, 50):
        # url 생성
		request_url_upcoming = f"https://api.themoviedb.org/3/movie/upcoming?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        # 요청한 데이터를 json형태로 변환하여 변수 movies에 저장
        # movies는 딕셔너리 형태의 데이터임
		movie_lists = requests.get(request_url_upcoming).json()
        # 영화 리스트 데이터는 현재 results가 key인 value에 리스트 형태로 저장되어 있음
		for movie_list in movie_lists['results']:
			# posterpath와 overview가 없는 값은 가져오지 않음
			if movie_list.get('overview') != '' and movie_list.get('poster_path') != None and movie_list.get('release_date') != None:
            # if movie_list.get('release_date', ''):
				fields = {
					'movie_user_like' : [],
					'title': movie_list['title'],
					'overview': movie_list['overview'],
					'release_date': movie_list['release_date'],
					'popularity': movie_list['popularity'],
					'poster_path': movie_list['poster_path'],
					'video': movie_list['video'],
					'vote_average': movie_list['vote_average'],
					'genre_ids': movie_list['genre_ids'],
					'genre_check': [],
					's_user_like' : [],
					'n_user_like' : [],
					't_user_like' : [],
					'f_user_like' : []
					}

				data = {
					"model": "movies.movie",
					"pk": movie_list['id'],
					"fields": fields
					}

				result_data.append(data)
    
    
	for i in range(1, 50):
        # url 생성
		request_url_popular = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        # 요청한 데이터를 json형태로 변환하여 변수 movies에 저장
        # movies는 딕셔너리 형태의 데이터임
		movie_lists = requests.get(request_url_popular).json()
        # 영화 리스트 데이터는 현재 results가 key인 value에 리스트 형태로 저장되어 있음
		for movie_list in movie_lists['results']:
			# posterpath와 overview가 없는 값은 가져오지 않음
			if movie_list.get('overview') != '' and movie_list.get('poster_path') != None and movie_list.get('release_date') != None:
            # if movie_list.get('release_date', ''):
				fields = {
					'movie_user_like' : [],
					'title': movie_list['title'],
					'overview': movie_list['overview'],
					'release_date': movie_list['release_date'],
					'popularity': movie_list['popularity'],
					'poster_path': movie_list['poster_path'],
					'video': movie_list['video'],
					'vote_average': movie_list['vote_average'],
					'genre_ids': movie_list['genre_ids'],
					'genre_check': [],
					's_user_like' : [],
					'n_user_like' : [],
					't_user_like' : [],
					'f_user_like' : []
					}

				data = {
					"model": "movies.movie",
					"pk": movie_list['id'],
					"fields": fields
					}

				result_data.append(data)
    
    
	with open("movie_data.json", "w", encoding="utf-8") as w:
		json.dump(result_data, w, indent=2, ensure_ascii=False)

get_movie_data()


