from datetime import date
from django.db import models
from profilemanager.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

# Create your models here.
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=254, unique=True)
    pdf_invoice = models.FileField(upload_to='invoices/')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.invoice_number
    
    
class PostageSettings(models.Model):
    free_postage = models.DecimalField(max_digits=5, decimal_places=2, blank=False, help_text='Amount in € that TOTAL needs to be over for free delivery')
    standard_delivery = models.DecimalField(max_digits=5, decimal_places=2, blank=False, help_text='Cost of standard delivery - % of TOTAL')
    express_delivery = models.DecimalField(max_digits=5, decimal_places=2, blank=False, help_text='Cost of express delivery - % of TOTAL')
    
    def __int__(self):
        return self.free_postage
    

class Voucher(models.Model):
    voucher_code = models.CharField(blank=False, null=False, unique=True, help_text='Discount Code')
    start_date = models.DateField(blank=False, null=False, help_text='First Day of Validity')
    end_date = models.DateField(blank=False, null=False, help_text='Last Day of Validity ')
    discount = models.PositiveIntegerField(blank=False, null=False, help_text='Discount - % of TOTAL')
    
    @property
    def status(self):
        today = date.today()

        if self.start_date > today:
            return "Pending"
        elif self.start_date <= today <= self.end_date:
            return "Active"
        else:
            return "Expired"
    
    def __str__(self):
        return self.voucher_code
    
class Newsletter(models.Model):
    newsletter_email = models.EmailField(blank=False, null=False)
    
    def __str__(self):
        return self.newsletter_email
    
    @receiver(post_save, sender=UserProfile)
    def create_newsletter_subscription(sender, instance, created, **kwargs):
        if created:
            if instance.user.email not in Newsletter.objects.values_list('newsletter_email', flat=True):
                Newsletter.objects.create(newsletter_email=instance.user.email)
        if not created:
            if instance.user.email not in Newsletter.objects.values_list('newsletter_email', flat=True):
                if instance.marketing_email:
                    Newsletter.objects.create(newsletter_email=instance.user.email)
            else:
                if not instance.marketing_email:
                    newsletter_instance = Newsletter.objects.get(newsletter_email=instance.user.email)
                    newsletter_instance.delete()
                
class NewsletterEmail(models.Model):
    
    EMAIL_STATUS = ((0, "Draft"), (1, "Sent"))
    
    subject = models.CharField(max_length=200, blank=False, null=False)                
    body = RichTextField(max_length=10000, null=False, blank=False)
    to_address = models.ManyToManyField(Newsletter, blank=False)
    status = models.IntegerField(choices=EMAIL_STATUS, default=0)
    date_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject