from django.core.management.base import BaseCommand
import os
import json
from forum.models import Book,Chapter,Verse

class Command(BaseCommand):
    help = "聖書をデータベースに追加"

    def handle(self, *args, **options):
        for curDir,dirs,files, in os.walk("bibles/en-bsb"):
            for file in files:
                text = os.path.join(curDir, file)
                with open(text,"r",encoding="utf-8") as context:
                    data = json.load(context)
                #print(file+"は" + text.split("/")[1] +"という聖書の" + text.split("/")[3] + "という書の" + text.split("/")[5] + "章" + file.split(".")[0] + "節です。")
                #print("内容は" + data["text"])

                if not "data" in data:
                    name = text.split("/")[3]
                    chapter_number = text.split("/")[5]
                    verse_number = file.split(".")[0]
                    verse_text = data["text"]
                
                    book, _ = Book.objects.get_or_create(name=name)
                    chapter, _ = Chapter.objects.get_or_create(book=book, chapter_number=chapter_number)
                    verse, _ = Verse.objects.get_or_create(chapter=chapter, verse_number=verse_number, text=verse_text)

        
