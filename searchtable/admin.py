from django.contrib import admin
from .models import Corporation

# Register your models here.
class CorporationAdmin(admin.ModelAdmin):
    list_display = ('name','corp_code', 'current_stock', 'market_cap', 'quarter')

admin.site.register(Corporation, CorporationAdmin)