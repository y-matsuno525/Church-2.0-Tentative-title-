from django.urls import path
from . import views
from .models import Book,Chapter,Verse

urlpatterns = [
    path('',views.list,name='list'),
    path("book/",views.book,name="book"),
    path("book/forum/",views.forum,name="forum"),
]

