from django.shortcuts import render
from .models import Book

books = Book.objects.all()

def list(request):

    params = {
        "books":books
    }

    return render(request,'forum/list.html',params)

def book(request):
    verses = []
    title = request.GET["name"]
    book = Book.objects.filter(name=title)
    chapters = book.chapter_set.all()
    for chapter in chapters:
        verses.append(chapter.verse_set.all())
    params = {
        "book":book,
        "chapters":chapters,
        "verses":verses
    }
    return render(request,"forum/book.html",params)
