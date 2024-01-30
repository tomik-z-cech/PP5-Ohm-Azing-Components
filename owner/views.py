from django.shortcuts import render
from django.views import generic

# Create your views here.
class OwnerMainView(generic.ListView):
    """
    View generates main view for owner (site admin)
    """

    template_name = "owner/owner.html"  # Template

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                "all_categories": 1,
            },
        )