from django.contrib import admin
from .models import FuelQuote
# Register your models here.

class FuelQuoteAdmin(admin.ModelAdmin):
  list_display = ('id','user','delivery_date' ,'delivery_state', 'total_amount_due')
  list_display_links = ('user', 'delivery_date', 'total_amount_due')
admin.site.register(FuelQuote, FuelQuoteAdmin)
