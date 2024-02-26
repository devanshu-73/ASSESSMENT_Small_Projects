from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
import random
from .models import * 

# Create your views here.

# function for fetching person data

def data(f_username,f_password=None):
   # getting all the user data
   user=People.objects.get(username=f_username)
   print("user",user)
   if f_password:
      user=People.objects.get(username=f_username, password=f_password)      
   # creating a context for html
   context={
            "user":user,
         }
   return context

def home(request):
   if 'username' in request.session:
      context=data(request.session['username'])   
      return render(request, 'institute_app/index.html',context)
   
   return render(request, "institute_app/login.html")


def login(request):
   # if the user is already logged-in
   if 'username' in request.session:
      context=data(request.session['username'])   
      return render(request, 'institute_app/index.html',context)
   else:
      msg=None
      try:
         # getting user input from html
         print("=========>>> Login")
         user_username=request.POST.get('username')
         user_password=request.POST.get('password')
         print("=========>>>",user_username,user_password)
         
         if(user_username != None and user_password != None):
            # if the user input is correct get the user data as an object
            context=data(user_username,user_password)

            # creating a session, so the institute_app have an info that the user is logged-in or not
            request.session['username']=context['user'].username
            
            # rendering the dashboard
            print("========== render index")
            return render(request, 'institute_app/index.html',context)
         
      except Exception as e:
         print("===========>>> Error =",e)
         msg="Invalid Input Pls Enter Again"
         
      return render(request, "institute_app/login.html", {'msg':msg})
   


def logout(request):
   print("==============>>> logout")
   if "username" in request.session:
      # deleting the session to notify that the user is logged out
      del request.session['username']
   return redirect(reverse('login'))
