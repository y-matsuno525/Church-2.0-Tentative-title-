from django.core.management.base import BaseCommand
from transformers import pipeline
from forum.models import Book,Post,Chapter,Verse

import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from django.conf import settings

root_file_path = os.path.join(settings.MEDIA_ROOT, "wordcloud") + "/"

class Command(BaseCommand):

    help = "Visualization of bulletin board"

    def handle(self, *args, **options):

        books = Book.objects.all()

        for book in books:

            chapters = Chapter.objects.filter(book=book)

            for chapter in chapters:

                verses = Verse.objects.filter(chapter=chapter)

                for verse in verses:

                    posts = Post.objects.filter(verse=verse)
                    
                    if posts.exists():

                        post_list = []

                        for post in posts:

                            post_list.append(post.text)

                        post_join = '\n'.join(post_list)

                        
                        file_name = book.name+"_"+str(chapter.chapter_number)+"_"+str(verse.verse_number)+".png"
                        file_path = root_file_path + file_name

                        if os.path.exists(file_path):
                            os.remove(file_path)

                        wd = WordCloud(width=400, height=300, background_color='white').generate(post_join)
                        wd.to_file(file_path)

                        
                        
                        with open(file_path, "rb") as img_file:

                            url = os.path.join(settings.MEDIA_ROOT, "img/wordcloud")+"/"+file_name

                            if os.path.exists(url):
                                os.remove(url)
                        
                            verse.image.save(file_name,img_file)
                            verse.save()
                        
                        #表示する場合
                        #plt.figure(figsize=(8, 6))
                        #plt.imshow(im)
                        #plt.axis('off')
                        #plt.title(book.name+":"+str(chapter.chapter_number)+":"+str(verse.verse_number))

        posts = Post.objects.all()
        post_list = []

        if posts.exists():

            for post in posts:

                post_list.append(post.text)

            post_join = '\n'.join(post_list)
            wd = WordCloud(width=400, height=300, background_color='white').generate(post_join)
            file_name = "all.png"
            file_path = root_file_path + file_name
            wd.to_file(file_path)