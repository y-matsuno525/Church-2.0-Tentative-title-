from django.core.management.base import BaseCommand
import stripe
from django.http import JsonResponse
import json

class Command(BaseCommand):
    help = "テストコマンド"

    def handle(self, *args, **options):
        
        stripe.api_key = 'sk_test_51QM2PUBqD5txSTx2CKj3jmDHr2mA8OwXjvc0FeyGOdjPiyTWIt8RdrE6iKznM21nQ7GxBNxVRWNoAtMtzyBIB2Qt00bVFRLu3B'
     

        try:

            products = stripe.Product.list()

            for product in products:

                if product['active']:

                    prices = stripe.Price.list(product=product['id'])

                    print("product name is "+product['name'])

                    if not len(prices) == 1:

                        for price in prices:
                            print(price['nickname']+" : "+str(price['unit_amount'])+" "+str(price['currency']))

                    else:
                        print("It's "+str(price['unit_amount'])+" "+str(price['currency']))

        except Exception as e:
            self.stderr.write(f"Error: {str(e)}")


