from django.shortcuts import render
from django.views import generic

# Create your views here.
class CheckoutView(generic.ListView):
    
    template_name = "checkout/checkout.html"
    
    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name
        )