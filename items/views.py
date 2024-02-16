# Imports
from django.shortcuts import render
from django.views import generic


class AllItemsView(generic.ListView):
    """
    Class generates view of landing page
    """

    template_name = "items/all_items.html"

    def get(self, request, *args, **kwargs):
        """This method generates view of landing page"""
        # Render template
        return render(
            request,
            self.template_name,
            {
                "free_postage": 1
            },
        )
