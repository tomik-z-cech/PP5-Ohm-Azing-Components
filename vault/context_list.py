from django.shortcuts import get_object_or_404
from items.models import Item
from owner.models import PostageSettings

def vault_content(request):
    """
    Items in vault :
    [item_pk, size, value, quantity]
    Translated items for template
    [item_pk, size, value, quantity, item_name, image_1, price_per_unit]
    """
    subtotal = 0
    vault = request.session.get('vault', [])
    translated_vault_content = []
    for vault_item in vault:
        item_per_line = get_object_or_404(Item, pk=vault_item[0])
        # Translate each record in vault for template
        translated_vault_item = [vault_item[0],vault_item[1],vault_item[2],vault_item[3], item_per_line.item_name, item_per_line.image_1, item_per_line.price_per_unit]
        translated_vault_content.append(translated_vault_item)
        # Add price of each item to Subtotal
        price_per_line = item_per_line.price_per_unit * int(vault_item[1]) * int(vault_item[3])
        subtotal = subtotal + price_per_line
    # Free postage maths
    free_postage_point = PostageSettings.objects.filter(pk=1).first()
    free_postage_left = int(free_postage_point.free_postage) - int(subtotal)
    # Set dictionary
    vault_context = {
        "items_in_vault": len(vault),
        "subtotal": subtotal,
        "free_postage_left": free_postage_left,
        "vault_content": translated_vault_content
        
    }
    return vault_context