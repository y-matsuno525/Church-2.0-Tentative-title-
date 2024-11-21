from django.shortcuts import render,redirect
from django.http import HttpResponse
import openai 
from forum.models import Post_test
from urllib.parse import urlparse, parse_qs

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

    previous_path = request.META.get('HTTP_REFERER')  # 一つ前のURLパスを取得

    parsed_url = urlparse(previous_path)
    query_params = parse_qs(parsed_url.query)

    #工夫すべき
    if previous_path in [
        "http://127.0.0.1:8000/menu/",
        "http://127.0.0.1:8000/accounts/login/",
        "http://127.0.0.1:8000/accounts/signup/",
        "http://127.0.0.1:8000/store/product_list/",
    ]:
        return redirect(previous_path)

    
    parent_path = '/'.join(previous_path.rstrip('/').split('/')[:-1]) + '/'  # 1階層上のURLを計算

    if 'name' in query_params:
        parent_path += f"?name={query_params['name'][0]}"  # リストの最初の要素を使用

        if 'chapter' in query_params:
            parent_path += f"&chapter={query_params['chapter'][0]}"

            if 'verse' in query_params:
                parent_path += f"&verse={query_params['verse'][0]}"

    return redirect(parent_path)