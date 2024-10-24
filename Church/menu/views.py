from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET['name']
    return HttpResponse("Hello " + name + "!! Here is Church3.0.")
