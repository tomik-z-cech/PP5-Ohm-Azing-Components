# PEP8
# Imports
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from owner.models import PostageSettings, Newsletter
from owner.forms import NewsletterForm
from items.models import Item, Category


class LandingPageView(generic.ListView):
    """
    Class generates view of landing page
    """

    template_name = "landing/index.html"
    model = Newsletter

    def get(self, request, *args, **kwargs):
        """
        This method generates view of landing page
        """
        # Get free postage info
        free_postage_treshold = PostageSettings.objects.filter(pk=1).first()
        # Get 3 newest items
        new_arrivals = Item.objects.all().order_by("-date_added")[:3]
        # Get 3 best rated items
        all_items = Item.objects.all()
        sorted_by_likes = sorted(
            all_items, key=lambda item: item.rating_counter(), reverse=True
        )
        favourites = sorted_by_likes[:3]
        # Render template
        return render(
            request,
            self.template_name,
            {
                "free_postage": free_postage_treshold.free_postage,
                "newsletter_form": NewsletterForm(),
                "new_arrivals": new_arrivals,
                "favourites": favourites,
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Method is used to add user to newsletter database
        """
        # Get the form with users email
        newsletter_form = NewsletterForm(request.POST)
        # Get postage settings from database
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        # Get 3 newest items
        new_arrivals = Item.objects.all().order_by("date_added")[:3]
        # Get 3 best rated items
        all_items = Item.objects.all()
        sorted_by_likes = sorted(
            all_items, key=lambda item: item.rating_counter(), reverse=True
        )
        favourites = sorted_by_likes[:3]
        # If form valid
        if newsletter_form.is_valid():
            # Get the email address from form
            submitted_email = newsletter_form.cleaned_data["newsletter_email"]
            # Check if users email isn't in database already
            if submitted_email not in Newsletter.objects.values_list(
                "newsletter_email", flat=True
            ):
                # If not, add user to mailing database
                newsletter_form.save()
                messages.success(
                    request,
                    f"Email {submitted_email} added to our mailing list.",
                )
            # If user already in databse, let the user know
            else:
                messages.error(
                    request,
                    f"Email {submitted_email} is already in mailing list.",
                )
        # Return back to ladning page
        return render(
            request,
            self.template_name,
            {
                "free_postage": postage_settings.free_postage,
                "newsletter_form": NewsletterForm(),
                "new_arrivals": new_arrivals,
                "favourites": favourites,
            },
        )


class SearchView(generic.ListView):
    """
    Class for search function
    """

    template_name = "landing/search_results.html"

    def get(self, request, *args, **kwargs):
        """
        Method get, not used, just to eliminate errors
        """
        # Redirect back to landing page
        return redirect("home")

    def post(self, request, *args, **kwargs):
        """
        Method used to search for users queries
        """
        # Get search term from form
        search_term = request.POST.get("search-query", "")
        # If search term exists
        if search_term:
            # Filter in category names
            categories_results = Category.objects.filter(
                category_name__icontains=search_term
            )
            # Filter in item names and item descriptions
            items_results = Item.objects.filter(
                Q(item_name__icontains=search_term)
                | Q(item_description__icontains=search_term)
            )
        # Render search results template
        return render(
            request,
            self.template_name,
            {
                "search_term": search_term,
                "categories_results": categories_results,
                "items_results": items_results,
                "total_results": len(items_results) + len(categories_results),
            },
        )
