from django.urls import path
from . import views

app_name = "userpage"

urlpatterns = [
    #path('',views.userpage),
    path('<str:username>/',views.userpage, name="userpage"),

]

