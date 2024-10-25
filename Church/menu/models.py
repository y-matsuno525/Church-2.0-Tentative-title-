from django.db import models

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

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.chapter_number}:{self.verse_number}"
