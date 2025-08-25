from django.contrib import admin
from . models import paymentMethod

# Register your models here.
class paymentMet(admin.ModelAdmin):
    list_display = ('payId','payerName','amount','date','cauuse','invoices_url')

admin.site.register(paymentMethod,paymentMet)
