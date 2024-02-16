from django.urls import path
from . import views

urlpatterns = [
    path('comments', views.comment_list),
    path('comments/<int:pk>/', views.comment_detail),
]
