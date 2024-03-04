from django.http import HttpResponse

class StripeWH_Handler:
    
    def __init__(self, request):
        self.request = request
        
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
        
    def handle_payment_success(self,event):
        return HttpResponse(
            content=f'Payment suceeded : {event["type"]}',
            status=200)
        
    def handle_payment_failed(self,event):
        return HttpResponse(
            content=f'Payment failed : {event["type"]}',
            status=200)