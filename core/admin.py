from django.contrib import admin
from django.utils.html import format_html
from urllib.parse import quote

from .models import Product, Batch, Shipment


admin.site.register(Product)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch_code', 'product', 'show_qr')

    def show_qr(self, obj):
        verify_url = f"https://pharma-tracker-qprq.onrender.com/verify/{obj.batch_code}/"
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=120x120&data={quote(verify_url)}"

        return format_html(
            '<img src="{}" width="120" height="120" />',
            qr_url
        )

    show_qr.short_description = "Show QR"


admin.site.register(Shipment)