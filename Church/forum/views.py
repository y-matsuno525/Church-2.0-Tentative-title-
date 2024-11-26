from django.shortcuts import render, get_object_or_404
from .models import Book,Post,Chapter,Verse
from .forms import DiscussionForm,PageForm,DiscussionForm_guest
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_ratelimit.decorators import ratelimit

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
        "form":PageForm(),
        
    }

    if (request.method == 'POST'):
        num = int(request.POST["page_number"])
        params["verses"] = page.get_page(num)


    return render(request,"forum/book.html",params)

def forum(request):

    name = request.GET["name"]
    chapter_number = request.GET["chapter"]
    verse_number = request.GET["verse"]

    book = Book.objects.filter(name=name).first()
    chapter = Chapter.objects.filter(book=book, chapter_number=chapter_number).first()
    verse=Verse.objects.filter(verse_number=verse_number, chapter=chapter).first()


    post = Post.objects.filter(verse__chapter__book__name = name, verse__chapter__chapter_number=chapter_number, verse__verse_number=verse_number).order_by("-created_at")

    can_post = 1

    if request.user.is_authenticated:
        form = DiscussionForm()
            
    else:
        form = DiscussionForm_guest()
            
    params = {

        "name":book.name,
        "chapter":chapter,
        "verse":verse,
        "form":form,
        "post":post,
        "can_post" : can_post

    }

    if (request.method == 'POST'):

        was_limited = False#ratelimit(key='ip', rate='5/m', method='POST', block=False)(lambda x: True)(request)

        if not was_limited:

            params["can_post"] = 1

            if request.user.is_authenticated:

                user = request.user
                post_text = request.POST["text"]
                name=request.GET["name"]
                chapter=request.GET["chapter"]
                verse_number=request.GET["verse"]
                post_verse = Verse.objects.get(verse_number=verse_number, chapter__chapter_number=chapter, chapter__book__name=name)

                post = Post(owner=user,text=post_text,verse=post_verse)     
                post.save() 
                params["post"] = Post.objects.filter(verse__chapter__book__name = name, verse__chapter__chapter_number=chapter_number, verse__verse_number=verse_number).order_by("-created_at")



            else:
                guest_name = request.POST["guest_name"]
                post_text = request.POST["text"]
                name=request.GET["name"]
                chapter=request.GET["chapter"]
                verse_number=request.GET["verse"]
                post_verse = Verse.objects.get(verse_number=verse_number, chapter__chapter_number=chapter, chapter__book__name=name)

                post = Post(guest_name=guest_name,text=post_text,verse=post_verse)     
                post.save() 
                params["post"] = Post.objects.filter(verse__chapter__book__name = name, verse__chapter__chapter_number=chapter_number, verse__verse_number=verse_number).order_by("-created_at")

        else:
            params["can_post"] = 0

    return render(request,"forum/forum.html",params)
