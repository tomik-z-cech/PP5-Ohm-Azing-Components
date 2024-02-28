

def vault_content(request):
    """
    
    """
    vault = request.session.get('vault', [])
    print(vault)
    vault_context = {
        "items_in_vault": len(vault),
    }
    return vault_context