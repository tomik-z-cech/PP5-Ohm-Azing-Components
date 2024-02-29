from django.shortcuts import get_object_or_404
from items.models import Item
from owner.models import PostageSettings

def vault_content(request):
    """
    [item_pk, size, value, quantity]
    """
    subtotal = 0
    vault = request.session.get('vault', [])
    for vault_item in vault:
        item_per_line = get_object_or_404(Item, pk=vault_item[0])
        price_per_line = item_per_line.price_per_unit * int(vault_item[1]) * int(vault_item[3])
        subtotal = subtotal + price_per_line
    free_postage_point = PostageSettings.objects.filter(pk=1).first()
    free_postage_left = int(free_postage_point.free_postage) - int(subtotal)
    vault_context = {
        "items_in_vault": len(vault),
        "subtotal": subtotal,
        "free_postage_left": free_postage_left,
        "vault_content": vault,
    }
    return vault_context