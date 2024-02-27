from django.shortcuts import render, redirect
from django.contrib import messages
from .models import People

def index(request):
    if 'username' in request.session:
        # User is logged in, render home page
        username = request.session['username']
        try:
            user = People.objects.get(username=username)
            context = {"user": user}
            return render(request, 'institute_app/index.html', context)
        except People.DoesNotExist:
            # If session username doesn't match any user, clear the session and render login
            del request.session['username']
    # User is not logged in, render login page
    return render(request, "institute_app/login.html")

def login(request):
    if 'username' in request.session:
        return redirect('index')  # Redirect to index if user is already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            try:
                user = People.objects.get(username=username, password=password)
                request.session['username'] = user.username
                return redirect('index')
            except People.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please provide both username and password.')
    
    return redirect('index')  # Redirect to index in case of GET request or login failure

def logout(request):
    if "username" in request.session:
        del request.session['username']
    return redirect('index')
