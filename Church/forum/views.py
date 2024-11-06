from django.shortcuts import render, get_object_or_404
from .models import Book,Post_test
from .forms import DiscussionForm
from django.core.paginator import Paginator

bible_order = [
        "genesis", "exodus", "leviticus", "numbers", "deuteronomy", "joshua",
        "judges", "ruth", "1samuel", "2samuel", "1kings", "2kings", "1chronicles", 
        "2chronicles", "ezra", "nehemiah", "esther", "job", "psalms", "proverbs", 
        "ecclesiastes", "songofsongs", "isaiah", "jeremiah", "lamentations", 
        "ezekiel", "daniel", "hosea", "joel", "amos", "obadiah", "jonah", 
        "micah", "nahum", "habakkuk", "zephaniah", "haggai", "zechariah", "malachi",
        "matthew", "mark", "luke", "john", "acts", "romans", "1corinthians", 
        "2corinthians", "galatians", "ephesians", "philippians", "colossians", 
        "1thessalonians", "2thessalonians", "1timothy", "2timothy", "titus", 
        "philemon", "hebrews", "james", "1peter", "2peter", "1john", "2john", 
        "3john", "jude", "revelation"
    ]

books = Book.objects.filter(name__in=bible_order)
ordered_books = sorted(books, key=lambda x: bible_order.index(x.name.lower()))

def list(request):
    
    params = {
        "books":ordered_books,
    }

    return render(request,'forum/list.html',params)

def book(request,num=1):

    book_name = request.GET.get("name")

    num = request.GET.get("page")

    if num is None:
        page = 1
    
    verses = []
    book = get_object_or_404(Book, name=book_name)
    chapters = book.chapter_set.all().order_by("chapter_number")
    for id,chapter in enumerate(chapters):
        verse_set = chapter.verse_set.all().order_by("verse_number")
        verses.append((verse_set,id+1))

    page = Paginator(verses,1)

    params = {
        "book":book_name,
        "chapters":chapters,
        "verses":page.get_page(num),
    }

    return render(request,"forum/book.html",params)

def forum(request):

    name=request.GET["name"]
    chapter=request.GET["chapter"]
    verse=request.GET["verse"]

    post = Post_test.objects.all()

    params = {
        "name":name,
        "chapter":chapter,
        "verse":verse,
        "form":DiscussionForm(),
        "post":post

    }

    if (request.method == 'POST'):
        post_name = request.POST["name"]
        post_text = request.POST["text"]
        post = Post_test(name=post_name,text=post_text)     
        post.save() 

    return render(request,"forum/forum.html",params)
