from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.views import generic
from items.models import Item

# Create your views here.
def add_to_vault(request, item_pk):
    """
    Method adds item to vault in format :
    [item_pk, size, value, quantity]
    """
    vault = request.session.get('vault', [])
    item_selected = get_object_or_404(Item, pk=item_pk)
    quantity = request.POST['quantity']
    size = request.POST.get('size', 1)
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
        for vault_item in vault:
            if vault_item[0] == item_pk and int(vault_item[3]) > int(item_selected.item_stock):
                messages.error(request, f'The amount of {item_selected.item_name} you trying to add to vault is higher than the stock amount.')
            else:
                request.session['vault'] = vault
                messages.warning(request, f'Item {item_selected.item_name} was added to vault.')
    else:
        item_to_add = [item_pk, size, value, quantity]
        vault.append(item_to_add)
        request.session['vault'] = vault
        messages.warning(request, f'Item {item_selected.item_name} was added to vault.')
    return redirect('item-detail', item_pk=item_pk)


class DisplayVaultItemsView(generic.ListView):

    template_name = "vault/vault.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
        )
        
    def post(self, request, *args, **kwargs):
        vault_item = int(request.POST.get('vault-item', 0))
        new_quantity = request.POST.get('quantity', 0)
        if new_quantity.isdigit():
            vault = request.session.get('vault', [])
            vault[vault_item][3] = int(new_quantity)
            item_selected = get_object_or_404(Item, pk=vault[vault_item][0])
            request.session['vault'] = vault
            messages.warning(request, f'Quantity of {item_selected.item_name} was changed.')
        else:
            messages.error(request, "Quantity couldn't be updated. Input wasn't a valid quantity.")
        return redirect('vault')
        

class RemoveVaultItemView(generic.ListView):
    
    def get(self, request, vault_item, *args, **kwargs):
        vault = request.session.get('vault', [])
        item_selected = get_object_or_404(Item, pk=vault[vault_item][0]) 
        vault.pop(vault_item)
        request.session['vault'] = vault
        messages.warning(request, f'Item {item_selected.item_name} was removed from vault.')
        return redirect('vault')
    
class ClearVaultView(generic.ListView):
    
    def get(self, request, *args, **kwargs):
        vault = request.session.get('vault', [])
        vault = []
        request.session['vault'] = vault
        messages.info(request, 'All items were removed from Vault.')
        return redirect('vault')