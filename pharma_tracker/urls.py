from django.contrib import admin
from django.urls import path
from core.views import home, verify_batch, reset_admin, seed_demo_data, qr_code, test_url

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('verify/<str:code>/', verify_batch, name='verify_batch'),
    path('reset-admin/', reset_admin),
    path('seed-demo-data/', seed_demo_data),
    path('qr/<str:code>/', qr_code, name='qr_code'),
    path('test-url/', test_url),
]