from django.shortcuts import render
from django.http import HttpResponse
from .models import Batch
from datetime import date

def home(request):
    code = request.GET.get('code')

    if code:
        return verify_batch(request, code)

    return render(request, 'core/home.html')


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
    
from django.contrib.auth.models import User
from django.http import HttpResponse

def reset_admin(request):
    user, created = User.objects.get_or_create(username='yashraj')
    user.is_staff = True
    user.is_superuser = True
    user.set_password('Admin@12345')
    user.save()
    return HttpResponse("Admin password reset successfully")