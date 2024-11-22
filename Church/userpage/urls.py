from django.urls import path
from . import views

app_name = "userpage"

urlpatterns = [
    path('<str:username>/',views.userpage),
    path('',views.userpage, name="userpage"),

]

