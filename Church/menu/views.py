from django.shortcuts import render,redirect
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

def back(request):
    previous_path = request.META['HTTP_REFERER']  # 一つ前のURLパスを取得

    #工夫すべき
    if (previous_path == "http://127.0.0.1:8000/menu/") or (previous_path == "http://127.0.0.1:8000/accounts/login/")or (previous_path == "http://127.0.0.1:8000/accounts/signup/")or (previous_path == "http://127.0.0.1:8000/store/product_list"):

        return redirect(previous_path)
    
    parent_path = '/'.join(previous_path.rstrip('/').split('/')[:-1]) + '/'  # 1階層上のURLを計算

    return redirect(parent_path)