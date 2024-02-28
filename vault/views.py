from django.shortcuts import redirect

# Create your views here.
def add_to_vault(request, item_pk):
    # vault = []
    vault = request.session.get('vault', [])
    print(request.POST)
    # vault.append(item_pk)
    request.session['vault'] = vault
    return redirect('item-detail', item_pk=item_pk)