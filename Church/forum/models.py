from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()

    def __str__(self):
        return f"{self.book.name} {self.chapter_number}"

class Verse(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    verse_number = models.IntegerField()
    text = models.TextField()
    image = models.ImageField(upload_to='img/wordcloud/',null=True)

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.chapter_number}:{self.verse_number}"
    
class Post_test(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_owner")
    text = models.TextField()
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE, related_name="post")
    created_at = models.DateTimeField(auto_now_add=True)
