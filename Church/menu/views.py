from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        "name" : "Yuki",
    }
    return render(request,'menu/index.html',params)

