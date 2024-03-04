from django.http import HttpResponse
import time
import stripe

class StripeWH_Handler:
    
    def __init__(self, request):
        self.request = request
        
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
        
    def handle_payment_success(self,event):
        intent = event.data.object
        pid = intent.id
        vault = intent.metadata.vault
        save_info = intent.metadata.save_info
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        total = round((stripe_charge.amount / 100), 2)
        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        attempt = 1
        while attempt <= 15:
            attempt += 1
            time.sleep(1)
        print(total)
        return HttpResponse(
            content=f'Payment suceeded : {event["type"]}',
            status=200)
        
    def handle_payment_failed(self,event):
        return HttpResponse(
            content=f'Payment failed : {event["type"]}',
            status=200)