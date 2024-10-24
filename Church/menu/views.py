from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        "name" : "Yuki",
    }
    return render(request,'menu/index.html',params)

def board(request):
    return render(request,'menu/board.html')

def reading(request):
    return render(request,"menu/reading.html")
