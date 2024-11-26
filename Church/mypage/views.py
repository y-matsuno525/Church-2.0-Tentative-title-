from django.shortcuts import render
from django.contrib.auth.models import User
from dogmatics.models import Preprint,FormalPaper
from forum.models import Post
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def mypage(request):

    #user_nameをユニークにする
    user = request.user
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

    
    return render(request, 'mypage/mypage.html', params)

def preprint_delete(request,preprint_id):
        
    if request.method == "POST":

        preprint = get_object_or_404(Preprint, id=preprint_id)
        preprint.delete()

        return redirect('mypage:mypage')
    
    return redirect('mypage:mypage')