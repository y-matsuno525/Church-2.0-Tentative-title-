from django.contrib import admin
from .models import Book,Chapter,Verse,Post

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Verse)
admin.site.register(Post)