from django.shortcuts import render
from django.contrib.auth.models import User
from dogmatics.models import Preprint,FormalPaper
from forum.models import Post

# Create your views here.
def userpage(request, username):

    #user_nameをユニークにする
    #username = request.GET["username"]
    user = User.objects.filter(username=username).first()
    preprints = Preprint.objects.filter(author=user)
    formal_papers = []
    for preprint in preprints:
        if FormalPaper.objects.filter(preprint=preprint):
            formal_papers.append(FormalPaper.objects.filter(preprint=preprint))
    posts = Post.objects.filter(owner=user)


    params = {
        'user' : user,
        'preprints' : preprints,
        'formal_papers'  : formal_papers,
        'posts' : posts,
    }

    return render(request, 'userpage/userpage.html', params)

    