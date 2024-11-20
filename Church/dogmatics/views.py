from django.shortcuts import render,redirect
from .forms import PreprintForm
from .models import Preprint,FormalPaper
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def select(request):
    return render(request,"dogmatics/select.html")

def journal(request):

    formal_papers = FormalPaper.objects.all()

    params = {

        'formal_papers' : formal_papers

    }

    return render(request,"dogmatics/journal.html",params)

def preprint(request):

    preprints = Preprint.objects.order_by("created_at")

    params = {

        'preprints' : preprints

    }

    return render(request,"dogmatics/preprint.html",params)

@login_required(login_url="/accounts/login/")
def post(request):

    params = {
        'form' : PreprintForm(),
    }

    if (request.method == 'POST'):
        
        author = request.user
        title = request.POST["title"]
        content = request.POST["content"]

        preprint = Preprint(author=author,title=title,content=content)
        preprint.save()

        return render(request,"dogmatics/select.html",params)

    return render(request,"dogmatics/post.html",params)

def reading(request):

    id = request.GET["id"]
    preprint = Preprint.objects.get(id=id)
    num_stars = preprint.star_count()

    params = {

        'preprint' : preprint,
        'num_stars' : num_stars,

    }

    if (request.method == 'POST'):
        
        id = request.GET["id"]

        if not request.user.is_authenticated:

            base_url = reverse('dogmatics:reading')
            url = f"{base_url}?id={id}"
            return redirect(url)

        user = request.user
        preprint = Preprint.objects.get(id=id)

        if preprint.stars.filter(id=user.id).exists():

            preprint.stars.remove(user)

        else:

            preprint.stars.add(user)

        base_url = reverse('dogmatics:reading')
        url = f"{base_url}?id={id}"

        return redirect(url)

    return render(request,'dogmatics/reading.html',params)

def j_reading(request):

    id = request.GET["id"]
    formal_paper = FormalPaper.objects.get(id=id)
    
    params = {

        'formal_paper' : formal_paper,

    }

    return render(request,'dogmatics/j_reading.html',params)
