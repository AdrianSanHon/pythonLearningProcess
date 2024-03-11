from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):                     #Its called automatically with some request.
    return HttpResponse("Hello World")
