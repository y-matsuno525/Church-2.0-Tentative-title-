from django.core.management.base import BaseCommand
import os
import json

class Command(BaseCommand):
    help = "聖書をデータベースに追加"

    def handle(self, *args, **options):
        for curDir,dirs,files, in os.walk("bibles/test"):
            for file in files:
                text = os.path.join(curDir, file)
                with open(text,"r",encoding="utf-8") as context:
                    data = json.load(context)
                print(file+"は" + text.split("/")[1] +"という聖書の" + text.split("/")[3] + "という書の" + text.split("/")[5] + "章" + file.split(".")[0] + "節です。")
                print("内容は" + data["text"])