from django.contrib import admin
from .models import Product, Batch, Shipment
from django.utils.html import format_html

class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch_code', 'product', 'show_qr')

    def show_qr(self, obj):
        if obj.qr_code:
            return format_html('<img src="{}" width="100" height="100" />', obj.qr_code.url)
        return "No QR"

admin.site.register(Product)
admin.site.register(Shipment)
admin.site.register(Batch, BatchAdmin)
