from django.db import models
from .models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers
from movies.models import Movie

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'mbtis', 'genders')
        extra_kwargs = {'password': {'write_only': True}}  # 비밀번호 필드 설정

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        user.set_password(password)  # 비밀번호 설정
        user.save()
        return user
    

# 사용자가 '좋아요'한 영화 목록 조회
class UserMovieListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'genre_ids')
    

    # 좋아요 한 영화 목록
    like_movies = MovieSerializer(many=True)
    s_like_movies = MovieSerializer(many=True)
    n_like_movies = MovieSerializer(many=True)
    t_like_movies = MovieSerializer(many=True)
    f_like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        # 사용자 id, 좋아요한 영화 목록
        fields = ('id', 'like_movies', 's_like_movies', 'n_like_movies', 't_like_movies', 'f_like_movies')
        
        