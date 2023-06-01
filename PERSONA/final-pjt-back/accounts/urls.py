from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup),
    path('profile/', views.get_accounts),
    path('<int:user_pk>/user_like_movie/', views.user_like_movie),
    path('<int:user_pk>/user_like_reco/', views.user_like_reco),
    path('<int:user_pk>/user_mbti_reco/', views.user_mbti_reco),
]
