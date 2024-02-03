from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomImageInputCategory(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'owner/widgets/category_image.html'

