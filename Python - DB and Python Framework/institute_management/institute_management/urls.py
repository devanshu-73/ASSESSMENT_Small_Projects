from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', admin.site.urls), # Direct On 8000 Port
]
