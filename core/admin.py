from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Batch, Shipment


admin.site.register(Product)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch_code', 'product', 'show_qr')

    def show_qr(self, obj):
        return format_html(
            '<img src="/qr/{}/" width="120" height="120" />',
            obj.batch_code
        )

    show_qr.short_description = "Show QR"


admin.site.register(Shipment)