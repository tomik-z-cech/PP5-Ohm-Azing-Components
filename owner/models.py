from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=254, unique=True)
    pdf_invoice = models.FileField(upload_to='invoices/')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.invoice_number