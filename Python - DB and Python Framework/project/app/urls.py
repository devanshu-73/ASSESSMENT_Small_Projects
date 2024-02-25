from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
]



