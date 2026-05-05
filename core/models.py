from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File


class Product(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Batch(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    batch_code = models.CharField(max_length=100, unique=True)
    mfg_date = models.DateField()
    exp_date = models.DateField()
    quantity = models.IntegerField()

    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.batch_code

    def save(self, *args, **kwargs):
        
        qr_data = f"http://192.168.1.3:8000/verify/{self.batch_code}/"

        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')

        file_name = f'{self.batch_code}.png'
        self.qr_code.save(file_name, File(buffer), save=False)

        super().save(*args, **kwargs)


class Shipment(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    status = models.CharField(max_length=50)