from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomImageInputCategory(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'owner/widgets/category_image.html'

class CustomImageInputItem1(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'owner/widgets/item_image1.html'

class CustomImageInputItem2(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'owner/widgets/item_image2.html'
    
class CustomImageInputItem3(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'owner/widgets/item_image3.html'