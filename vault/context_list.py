from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item
from owner.models import PostageSettings

def vault_content(request):

    # bag_items = []
    # total = 0
    # product_count = 0
    # bag = request.session.get('bag', {})
    
    vault_items = []
    subtotal_price = 0
    items_count = 0
    vault = request.session.get('vault', {})
    postage_settings = PostageSettings.objects.filter(pk=1).first()
    print(postage_settings)
    
    context = {
        "postage_settings": postage_settings,
    }

    return context