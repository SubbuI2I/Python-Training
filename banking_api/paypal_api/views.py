#django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

#external 
from paypalrestsdk import payments

#application
from banking_api.settings import env

# Create your views here.
PAYPAL_CLIENT_ID =  env('PAYPAL_CLIENT_ID') 
PAYPAL_CLIENT_SECRET = env('PAYPAL_CLIENT_SECRET')
PAYPAL_MODE=env('PAYPAL_MODE')

def index(request):
    return render(request, 'paypal_api/index.html')

def payment(request):
    print(PAYPAL_CLIENT_ID, PAYPAL_MODE, PAYPAL_CLIENT_SECRET)
    try:
        payment_config = { "client_id" : PAYPAL_CLIENT_ID , 
                            "client_secret" :  PAYPAL_CLIENT_SECRET ,
                            "sandbox_mode" : True 
                         }
        payment_obj = Payment({
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "https://example.com/return",
                "cancel_url": "https://example.com/cancel"
            },
            "transactions": [{
                "amount": {
                    "total": "10.00",
                    "currency": "USD"
                },
                "description": "Payment description"
            }]
        },)  # Make sure the mode matches the value you set in the settings

        if payment_obj.create(payment_config):
            approval_url = payment.links[1].href
            return redirect(approval_url)
        else:
            messages.error(request, 'Error occured on connecting Paypal API')
    except Exception as ex:
        messages.error(request, 'Error occured while integrating Paypal API')
        print('error')
        return render(request, 'paypal_api/payment.html')
    return render(request, 'paypal_api/payment.html')

def payment_done(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')
    payment = Payment.find(payment_id)
    payment_config = {"client_id":PAYPAL_CLIENT_ID, "client_secret": PAYPAL_CLIENT_SECRET , "payer_id": payer_id}
    if payment.execute(payment_config):
        messages.success(request, 'Payment successful.')
        return render(request, 'payment_done.html')
    else:
        messages.error(request, 'An error occurred while processing your payment. Please try again later.')
        return render(request, 'payment_done.html')
        
def payment_cancelled(request):
    messages.info(request, 'Payment cancelled.')
    return render(request, 'payment_cancelled.html')
