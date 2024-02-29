from django.urls import path
from institute_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # URL for both login and home page
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('add_person/', views.add_person, name='add_person'),
    path('student/', views.student_detail_view, name='student_detail'),
    path('teacher/', views.teacher_detail_view, name='teacher_detail'),
    path('club/', views.club_detail_view, name='club_detail'),
    path('book/', views.book_detail_view, name='book_detail'),
    # path('changepassword/', views.changepassword, name='changepassword'),
]



