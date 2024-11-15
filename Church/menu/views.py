from django.shortcuts import render
from django.http import HttpResponse
import openai 
from forum.models import Post_test

def index(request):
    """
    texts = [{"role":"system","content":"以下の文章をまとめて、一つの体系的な教義を作ってください。"}]

    openai.api_key = "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"

    post = Post_test.objects.all()
    for p in post:
        texts.append({"role":"user","content":p.text})

    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  
    messages=texts,
    )


    
    sum = response.choices[0].message.content
    """
    params = {
        "name" : "Yuki",
        "sum": "Under Construction"
    }
    return render(request,'menu/index.html',params)

