from urllib import response
from django.shortcuts import render

# Exercise 1
def home(request):
    return render(request,'home.html')
