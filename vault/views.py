# PEP8
# Imports
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.views import generic
from items.models import Item


def add_to_vault(request, item_pk):
    """
    Method adds item to vault in format :
    [item_pk, size, value, quantity]
    """
    # Get current vault
    vault = request.session.get("vault", [])
    # Get item to add
    item_selected = get_object_or_404(Item, pk=item_pk)
    # Get quantity of item to add from request.POST
    quantity = request.POST["quantity"]
    # Get size of item to add from request.POST
    # Size 1 is default (item has no sizes)
    size = request.POST.get("size", 1)
    # Get value of item to add from reuqest.POST
    # Value 0 is default (item has no values)
    value = request.POST.get("value", 0)
    # If there are items in vault
    if len(vault) > 0:
        # For each item in vault
        for vault_item in vault:
            # Set variable append_new for purposes of same item with different
            # size or value
            append_new = True
            # If same item with same size and
            # same value already exists in Vault
            if (
                vault_item[0] == item_pk
                and vault_item[1] == size
                and vault_item[2] == value
            ):
                # Increase quantity
                vault_item[3] = int(vault_item[3]) + int(quantity)
                # Set append_new to false
                append_new = False
            # If item not in Vault yet
            else:
                # Set array for item to add
                item_to_add = [item_pk, size, value, quantity]
        # If new item is to be appended
        if append_new:
            # Append the item to running vault
            vault.append(item_to_add)
        # Loop through the vault to determine if quantity of item to add
        # is more than stock of item to add
        for vault_item in vault:
            # If not sufficient amount in stock
            if vault_item[0] == item_pk and int(vault_item[3]) > int(
                item_selected.item_stock
            ):
                messages.error(
                    request,
                    f"The amount of {item_selected.item_name} you trying \
                    to add to vault is higher than the stock amount.",
                )
            # If sufficient amount of item in stock
            else:
                # Save the vault content into session
                request.session["vault"] = vault
                messages.warning(
                    request,
                    f"Item {item_selected.item_name} was added to vault.",
                )
    # If there are no items in stock yet
    else:
        # Create array of item to add to vault
        item_to_add = [item_pk, size, value, quantity]
        # Append the item to vault
        vault.append(item_to_add)
        # Save the vault into session
        request.session["vault"] = vault
        messages.warning(
            request, f"Item {item_selected.item_name} was added to vault."
        )
    # Redirect back to item detail
    return redirect("item-detail", item_pk=item_pk)


class DisplayVaultItemsView(generic.ListView):
    """
    Class to display items in Vault
    """

    template_name = "vault/vault.html"

    def get(self, request, *args, **kwargs):
        """
        Method renders contents of vault into template
        """
        # Render template
        return render(
            request,
            self.template_name,
        )

    def post(self, request, *args, **kwargs):
        """
        Method updates quantity of item from vault template
        """
        # Get item to update
        vault_item = int(request.POST.get("vault-item", 0))
        # Get new quantity
        new_quantity = request.POST.get("quantity", 0)
        # Ensure the users input is only digit
        if new_quantity.isdigit():
            # Request current vault
            vault = request.session.get("vault", [])
            # Update quantity of upadted item
            vault[vault_item][3] = int(new_quantity)
            # Get updated item from database
            item_selected = get_object_or_404(Item, pk=vault[vault_item][0])
            # Save vault into session
            request.session["vault"] = vault
            messages.warning(
                request, f"Quantity of {item_selected.item_name} was changed."
            )
        # Input was not a number
        else:
            messages.error(
                request,
                "Quantity couldn't be updated. Input wasn't a valid quantity.",
            )
        # Redirect back to vault
        return redirect("vault")


class RemoveVaultItemView(generic.ListView):
    """
    Class removes selected item from vault
    """

    def get(self, request, vault_item, *args, **kwargs):
        """
        Method gets item and removes it from vault
        """
        # Get content of vault from session
        vault = request.session.get("vault", [])
        # Get details of item to be removed
        item_selected = get_object_or_404(Item, pk=vault[vault_item][0])
        # Remove requested item from vault array
        vault.pop(vault_item)
        # Save vault to session
        request.session["vault"] = vault
        messages.warning(
            request, f"Item {item_selected.item_name} was removed from vault."
        )
        # Redirect back to vault
        return redirect("vault")


class ClearVaultView(generic.ListView):
    """
    Class clears the entire content of vault
    """

    def get(self, request, *args, **kwargs):
        """
        Method clears the vault entirely
        """
        # Get the vault from session
        vault = request.session.get("vault", [])
        # Set vault to empty array
        vault = []
        # Save vault to session
        request.session["vault"] = vault
        messages.info(request, "All items were removed from Vault.")
        # Redirect back to vault
        return redirect("vault")
