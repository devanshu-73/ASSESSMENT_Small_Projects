from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/comments', views.comment_list),
    path('api/comments/<int:pk>/', views.comment_detail),
]

# API_URL : http://127.0.0.1:8000/api/comments/
# API_URL_One_DATA : http://127.0.0.1:8000/api/comments/1/