# Imports
from django.shortcuts import render
from django.views import generic


class LandingPageView(generic.ListView):
    """
    Class generates view of landing page
    """

    template_name = "landing/index.html"

    def get(self, request, *args, **kwargs):
        """This method generates view of landing page"""
        # Render tamplate
        return render(
            request,
            self.template_name,
            {
            },
        )
