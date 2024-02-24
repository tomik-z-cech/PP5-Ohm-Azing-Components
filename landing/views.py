# Imports
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from owner.models import PostageSettings, Newsletter
from owner.forms import NewsletterForm



class LandingPageView(generic.ListView):
    """
    Class generates view of landing page
    """

    template_name = "landing/index.html"
    model = Newsletter

    def get(self, request, *args, **kwargs):
        """This method generates view of landing page"""
        # Render template
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        return render(
            request,
            self.template_name,
            {
                "free_postage": postage_settings.free_postage,
                "newsletter_form": NewsletterForm()
            },
        )
        
    def post(self, request, *args, **kwargs):
        newsletter_form = NewsletterForm(request.POST)
        # Render template
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        if newsletter_form.is_valid():
            submitted_email = newsletter_form.cleaned_data['newsletter_email']
            if submitted_email not in Newsletter.objects.values_list('newsletter_email', flat=True):
                newsletter_form.save()
                messages.success(request, f'Email address {submitted_email} successfully added to our mailing list.')
            else:
                messages.error(request, f'Email address {submitted_email} is already on our mailing list.')
        print(Newsletter.objects.all())
        return render(
            request,
            self.template_name,
            {
                "free_postage": postage_settings.free_postage,
                "newsletter_form": NewsletterForm()
            },
        )
        
