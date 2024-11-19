from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('checkout',views.checkout,name='checkout'),
    path('success',views.success,name='success'),
    path('cancel',views.cancel,name='cancel'),
    path('create-checkout-session',views.create_checkout_session,name='cancel'),
    path('webhook', views.handle_webhook, name='webhook'),
    path('product_list', views.product_list, name='product_list'),
]