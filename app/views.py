from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def vijay(request):
    return HttpResponse('<marquee><h1>vijay is bad boy</h1></marquee>')
