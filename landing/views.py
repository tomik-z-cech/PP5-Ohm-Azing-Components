# Imports
from django.shortcuts import render
from django.views import generic
from owner.models import PostageSettings


class LandingPageView(generic.ListView):
    """
    Class generates view of landing page
    """

    template_name = "landing/index.html"

    def get(self, request, *args, **kwargs):
        """This method generates view of landing page"""
        # Render tamplate
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        return render(
            request,
            self.template_name,
            {
                "free_postage": postage_settings.free_postage
            },
        )
