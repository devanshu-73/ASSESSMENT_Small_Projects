from django.shortcuts import render

# Create your views here.
def index(request):
    return render("<h1>Hello</h1>")