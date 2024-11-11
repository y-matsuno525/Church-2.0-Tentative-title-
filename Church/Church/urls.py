from django.contrib import admin
from django.urls import path,include
import menu.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('menu/',include('menu.urls')),
    path("accounts/", include("accounts.urls")),
]
