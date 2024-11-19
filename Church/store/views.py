import stripe
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

stripe.api_key = 'sk_test_51QM2PUBqD5txSTx2CKj3jmDHr2mA8OwXjvc0FeyGOdjPiyTWIt8RdrE6iKznM21nQ7GxBNxVRWNoAtMtzyBIB2Qt00bVFRLu3B'


def checkout(request):
    return render(request, "store/checkout.html")


def success(request):
    return render(request, "store/success.html")


def cancel(request):
    return render(request, "store/cancel.html")

def product_list(request):

    products = stripe.Product.list()

    if not products:
        print("!エラー!")

    products_list =[]

    for product in products:


        if product['active']:
            
            name = product['name']
            image = product['images']

            prices = stripe.Price.list(product=product['id'])

            price_list = []
            num = len(prices)

            for p_price in prices:

                nickname = p_price['nickname']
                price = str(p_price['unit_amount'])
                currency = p_price['currency']
                id = p_price['id']
               
                type_list = {

                            'price':price, 
                            'nickname':nickname,
                            'currency':currency,
                            'id':id,
                           
                             }
            
                price_list.append(type_list)

            product_list = {

                'name' : name,
                'image' : image,
                'price_list' : price_list, 
                'num' : num,

            }

        else:
            print(product["name"]+" is False.")

        products_list.append(product_list)

    params = {
        'products_list' : products_list
    }
    print(params)



    return render(request, "store/product_list.html", params)


@csrf_exempt
def create_checkout_session(request):

    if (request.method == 'POST'):
         
        price = request.POST["price"]
    
    checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price':price,
                'quantity':1
            },],
            mode='payment',
            success_url=
            'http://127.0.0.1:8000/store/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url= 'http://127.0.0.1:8000//store/cancel',)
    
    return render(request, 'store/checkout.html', {'checkout_url': checkout_session.url})

        # ここもう少しハンドリングするべき


endpoint_secret = 'whsec_7dfaa602ece8bbc9c1c974c457ddce66b205bcdfbb691b5422cefc4ec65f79c2'


@csrf_exempt
def handle_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        # Stripeが送ってきたものか判定
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        # Payloadが変な時
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Stripeでない第三者が不正に送ってきた時
        return HttpResponse(status=400)

    # eventのtypeによって、好きなように分岐
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        metadata = payment_intent["metadata"]
        print('決済が完了したのでここで決済処理をします！！！')
        print("決済の詳細情報→" + str(payment_intent))
        print("指定したメタデータの取り出し→" + str(metadata))

    else:
        event_type = event['type']
        print(f'Event type {event_type}')
    return HttpResponse(status=200)