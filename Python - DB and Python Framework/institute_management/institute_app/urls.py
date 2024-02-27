from django.urls import path
from institute_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # URL for both login and home page
    path('login/', views.login, name='login'),  # URL for login
    path('logout/', views.logout, name='logout'),  # URL for logout
]



