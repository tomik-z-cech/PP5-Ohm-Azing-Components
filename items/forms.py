# Imports
from items.models import ItemComments
from django import forms

class ItemCommentForm(forms.ModelForm):
    """Form for comments"""

    class Meta:
        model = ItemComments
        fields = ("comment_body",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["comment_body"].widget.attrs.update(
            {
                "rows": 3,
                "placeholder": "Type your comment here ...",
                "aria-label": "News Comment",
                'class': 'shadow-none',
            }
        )