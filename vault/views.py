from django.shortcuts import redirect

# Create your views here.
def add_to_vault(request, item_pk):
    """
    Method adds item to vault in format :
    [item_pk, size, value, quantity]
    """
    vault = request.session.get('vault', [])
    quantity = request.POST['quantity']
    size = request.POST.get('size', 0)
    value = request.POST.get('value', 0)
    if len(vault) > 0:
        for vault_item in vault:
            append_new = True
            if vault_item[0] == item_pk and vault_item[1] == size and vault_item[2] == value:
                vault_item[3] = int(vault_item[3]) + int(quantity)
                append_new = False
            else:
                item_to_add = [item_pk, size, value, quantity]
        if append_new:
            vault.append(item_to_add)
    else:
        item_to_add = [item_pk, size, value, quantity]
        vault.append(item_to_add)
    request.session['vault'] = vault
    return redirect('item-detail', item_pk=item_pk)