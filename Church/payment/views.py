from django.views import generic

import os
import stripe
import json
from django.urls import reverse
from django.shortcuts import redirect
from django.http import JsonResponse

class PaymentIndexView(generic.TemplateView):
   template_name = "payment/index.html"

class PaymentCheckoutView(generic.TemplateView):
   template_name = "payment/checkout.html"

class PaymentSuccessView(generic.TemplateView):
   template_name = "payment/success.html"

class PaymentCancelView(generic.TemplateView):
   template_name = "payment/cancel.html"

def create_checkout_session(request):
   stripe.api_key = 'sk_test_51QM2PUBqD5txSTx2CKj3jmDHr2mA8OwXjvc0FeyGOdjPiyTWIt8RdrE6iKznM21nQ7GxBNxVRWNoAtMtzyBIB2Qt00bVFRLu3B'

   try:
       checkout_session = stripe.checkout.Session.create(
           payment_method_types=['card'],
           line_items=[
               {
                   'price_data': {
                       'currency': 'usd',
                       'unit_amount': 2000,
                       'product_data': {
                           'name': 'Stubborn Attachments',
                           'images': ['https://i.imgur.com/EHyR2nP.png'],
                       },
                   },
                   'quantity': 1,
               },
           ],
           mode='payment',
           success_url=request.build_absolute_uri(reverse('payment:success')),
           cancel_url=request.build_absolute_uri(reverse('payment:cancel')),
       )
       return JsonResponse({'id': checkout_session.id})
   except Exception as e:
       return JsonResponse({'error':str(e)})