from django.urls import path,include
from . import views

app_name = "dogmatics"

urlpatterns = [
    path('',views.select,name='select'),
    path('journal',views.journal,name='journal'),
    path('journal/j_reading',views.j_reading,name='j_reading'),
    path('preprint/',views.preprint,name='preprint'),
    path('post/',views.post,name='post'),
    path('preprint/reading',views.reading,name='reading'),
    path('cant_post',views.cant_post,name='cant_post'),
]
