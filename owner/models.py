from django.db import models

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