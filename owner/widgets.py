# PEP8
# Imports
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomImageInputCategory(ClearableFileInput):
    """
    Class for category image widget
    """

    clear_checkbox_label = _("Remove")
    initial_text = _("Current Image")
    input_text = _("")
    template_name = "owner/widgets/category_image.html"


class CustomImageInputItem1(ClearableFileInput):
    """
    Class for item image 1 widget
    """

    clear_checkbox_label = _("Remove")
    initial_text = _("Current Image")
    input_text = _("")
    template_name = "owner/widgets/item_image1.html"


class CustomImageInputItem2(ClearableFileInput):
    """
    Class for item image 2 widget
    """

    clear_checkbox_label = _("Remove")
    initial_text = _("Current Image")
    input_text = _("")
    template_name = "owner/widgets/item_image2.html"


class CustomImageInputItem3(ClearableFileInput):
    """
    Class for item image 3 widget
    """

    clear_checkbox_label = _("Remove")
    initial_text = _("Current Image")
    input_text = _("")
    template_name = "owner/widgets/item_image3.html"
