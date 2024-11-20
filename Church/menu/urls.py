from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('list/',include('forum.urls')),
    path('dogmatics/',include('dogmatics.urls')),
    path('back/',views.back,name="back"),
]
