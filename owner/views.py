from django.shortcuts import render
from django.views import generic
from items.models import Category

# Create your views here.
class OwnerMainView(generic.ListView):
    """
    View generates main view for owner (site admin)
    """

    template_name = "owner/categories.html"  # Template

    def get(self, request, *args, **kwargs):
        all_categories = Category.objects.all()
        return render(
            request,
            self.template_name,
            {
                "all_categories": all_categories,
            },
        )