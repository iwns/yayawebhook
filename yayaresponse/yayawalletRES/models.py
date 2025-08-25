from django.db import models

# Create your models here.
class paymentMethod(models.Model):
    payId = models.CharField(primary_key=True,max_length=40)
    payerName = models.CharField(max_length=60)
    amount = models.IntegerField(blank=False)
    date = models.DateTimeField()
    cause = models.CharField(max_length=100)
    invoices_url = models.CharField(max_length=100,unique=True)