from django.shortcuts import render
from django.http import HttpResponse
from .models import Batch
from datetime import date

def home(request):
    return render(request, 'core/verify.html')

def verify_batch(request, code):
    try:
        batch = Batch.objects.get(batch_code=code)

        is_expired = batch.exp_date < date.today()

        return render(request, 'core/verify.html', {
            'batch': batch,
            'valid': not is_expired,
            'expired': is_expired
        })

    except Batch.DoesNotExist:
        return render(request, 'core/verify.html', {
            'valid': False
        })