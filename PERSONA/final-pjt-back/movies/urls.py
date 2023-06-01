from . import views
from django.urls import path

urlpatterns = [
  # movie
	path('movies/', views.movie_list),
	path('movies/<int:movie_pk>/', views.movie_detail),
	path('movies/<int:movie_pk>/likes/', views.likes),
 	path('movies/comments/<int:comment_pk>/', views.delete_comment),
	
	# comment 
	path('comments/', views.comment_list),
	path('comments/<int:comment_pk>/', views.comment_detail),
	path('movies/<int:movie_pk>/comments/', views.create_comment),

	# community
	path('community/<int:community_pk>/likes/', views.community_likes),
	path('community/', views.community_list),
	path('community/<int:community_pk>/', views.community_detail),
	# path('community/create/', views.create_community),
	path('community/<int:community_pk>/comments/<int:comment_pk>/', views.community_comment_delete),

	# genre
	path('moviegenre/', views.movie_genre),
	path('<int:sort_num>/sort/', views.genre_sort),
]