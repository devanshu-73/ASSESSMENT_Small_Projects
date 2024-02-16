from django.contrib import admin
from .models import *
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display= ['author','created_at'] 

admin.site.register(Comment)