# PEP8
# Imports
from datetime import date
from django.db import models
from profilemanager.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


class PostageSettings(models.Model):
    """
    Model for postage settings
    """

    free_postage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        help_text="Amount in € that VAULT needs to be over for free delivery",
    )
    standard_delivery = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        help_text="Cost of standard delivery - % of VAULT ",
    )
    express_delivery = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        help_text="Cost of express delivery - % of VAULT ",
    )
    minimum_order = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        help_text="Amount in € VAULT needs to be over",
    )

    def __int__(self):
        """`
        Initial method
        """
        return self.free_postage


class Voucher(models.Model):
    """
    Model for discount codes (vouchers)
    """

    voucher_code = models.CharField(
        blank=False, null=False, unique=True, help_text="Discount Code"
    )
    start_date = models.DateField(
        blank=False, null=False, help_text="First Day of Validity"
    )
    end_date = models.DateField(
        blank=False, null=False, help_text="Last Day of Validity "
    )
    discount = models.PositiveIntegerField(
        blank=False, null=False, help_text="Discount - % of TOTAL"
    )

    @property
    def status(self):
        """
        Property for checking vocuher status based on current date
        """
        today = date.today()

        # If strting date later than today
        # Voucher is PENDING
        if self.start_date > today:
            return "Pending"
        # If today is between startung and finishing date
        # Voucher is ACTIVE
        elif self.start_date <= today <= self.end_date:
            return "Active"
        # Otherwise EXPIRED
        else:
            return "Expired"

    def __str__(self):
        return self.voucher_code


class Newsletter(models.Model):
    """
    Model for keeping email addresses for newsletter mailer
    """

    newsletter_email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.newsletter_email

    # Receiver to add user into the list after registartion
    # or to manage preferences after editing user profile
    @receiver(post_save, sender=UserProfile)
    def create_newsletter_subscription(sender, instance, created, **kwargs):
        # If user created ...
        if created:
            # ... and not in the list already
            if instance.user.email not in Newsletter.objects.values_list(
                "newsletter_email", flat=True
            ):
                # Add user to mailing list
                Newsletter.objects.create(newsletter_email=instance.user.email)
        # If edited ...
        if not created:
            # ... and user prefernce is to be on the mailing list check and add
            if instance.user.email not in Newsletter.objects.values_list(
                "newsletter_email", flat=True
            ):
                if instance.marketing_email:
                    Newsletter.objects.create(
                        newsletter_email=instance.user.email
                    )
            # ... and user prefernece is not to be on the miling list
            # check and remove
            else:
                if not instance.marketing_email:
                    newsletter_instance = Newsletter.objects.get(
                        newsletter_email=instance.user.email
                    )
                    newsletter_instance.delete()


class NewsletterEmail(models.Model):
    """
    Model to hold drafts or already sent marketing emails
    """

    # Status of newsletter emails
    EMAIL_STATUS = ((0, "Draft"), (1, "Sent"))

    subject = models.CharField(max_length=200, blank=False, null=False)
    body = RichTextField(max_length=10000, null=False, blank=False)
    to_address = models.ManyToManyField(Newsletter, blank=False)
    status = models.IntegerField(choices=EMAIL_STATUS, default=0)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
