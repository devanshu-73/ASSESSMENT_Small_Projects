from django.urls import path
from institute_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.login,name='login'),
]



