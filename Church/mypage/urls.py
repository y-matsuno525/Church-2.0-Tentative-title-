from django.urls import path
from . import views

app_name = "mypage"

urlpatterns = [
    #path('',views.userpage),
    path('',views.mypage, name="mypage"),
    path('preprint_delete/<int:preprint_id>/',views.preprint_delete, name="preprint_delete"),

]

