from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('menu/',include('menu.urls')),
    path("accounts/", include("accounts.urls")),
    path("store/",include("store.urls")),
    path("userpage/",include("userpage.urls")),
    path("mypage/",include("mypage.urls")),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #後で理解