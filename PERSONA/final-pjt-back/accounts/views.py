import json
import random

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from movies.models import Movie
from movies.serializers import MovieSerializer, MovieListSerializer

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .serializers import UserSerializer, UserMovieListSerializer


# Create your views here.
@api_view(['POST'])
def signup(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()  # 사용자 데이터 저장	
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_accounts(request):
    User = get_user_model()
    user_pk = request.GET.get('user_pk')
    users = User.objects.all()

    data = []
    for user in users:
        if int(user.pk) == int(user_pk):
            data.append({
                'username': user.username,
                'user_id': user.pk,
                'genders': user.genders,  # 새로운 필드
                'mbtis': user.mbtis,  # 새로운 필드
            })

    return JsonResponse(data, safe=False)


def user_like_movie(request, user_pk):
    User = get_user_model()
    
    Users = get_object_or_404(User, pk=user_pk)
    serializer = UserMovieListSerializer(Users)
    like_lst = serializer.data.get('like_movies')
    
    return JsonResponse(like_lst, safe=False) 
    
def user_like_reco(request, user_pk):
    User = get_user_model()

    movies_json = open('./movies/fixtures/movie_data.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    genre_json = open('./movies/fixtures/genres.json', encoding='UTF8')
    genre_list = json.load(genre_json)
    
    
    Users = get_object_or_404(User, pk=user_pk)
    serializer = UserMovieListSerializer(Users)
    like_lst = serializer.data.get('like_movies')
    
    if like_lst:
        random_list = []
        for i in range(len(like_lst)):
            
            random_list.append(like_lst[i])
            
        random_movie = random.choices(random_list, k=1)[0]
    else:
        # order_by('?') 무작위로 정렬
        random_movie = Movie.objects.values('title', 'genre_ids').order_by('?').first()

    random_movie = random_movie['genre_ids'][1:-1].split(',')

    recommend_movies = []
    
    for movie in movies_list:
        for random_genre in random_movie:
            if int(random_genre) in movie['fields']['genre_ids']:
                if movie not in recommend_movies:
                    recommend_movies.append(movie)
                    continue
    
    final_reco = []
    if len(recommend_movies) >= 10:
        final_reco.append(random.sample(recommend_movies, 10))
    else:
        final_reco = recommend_movies
        
    return JsonResponse(final_reco, safe=False)
    


def user_mbti_reco(request, user_pk):
    User = get_user_model()
    movies_json = open('./movies/fixtures/movie_data.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    genre_json = open('./movies/fixtures/genres.json', encoding='UTF8')
    genre_list = json.load(genre_json)
    
    
    Users = get_object_or_404(User, pk=user_pk)
    user_mbtis = Users.mbtis

    movie_lists = Movie.objects.all()
    serializer = MovieListSerializer(movie_lists, many=True)

    like_lst = []
    if user_mbtis[0] == 'N':
        for i in range(len(serializer.data)):
            if serializer.data[i].get('n_user_like') and serializer.data[i] not in like_lst:
                like_lst.append(serializer.data[i])
    elif user_mbtis[0] == 'S':
        for i in range(len(serializer.data)):
            if serializer.data[i].get('s_user_like') and serializer.data[i] not in like_lst:
                like_lst.append(serializer.data[i])
    if user_mbtis[1] == 'T':
        for i in range(len(serializer.data)):
            if serializer.data[i].get('t_user_like') and serializer.data[i] not in like_lst:
                like_lst.append(serializer.data[i])
    elif user_mbtis[0] == 'F':
        for i in range(len(serializer.data)):
            if serializer.data[i].get('f_user_like') and serializer.data[i] not in like_lst:
                like_lst.append(serializer.data[i])
    
    random_list = []
    if len(like_lst) < 10:
        random_list = like_lst
    else:
        random_list.append(random.sample(like_lst, 10))
    
    return JsonResponse(random_list, safe=False)