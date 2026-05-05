from django.contrib import admin
from django.urls import path
from core.views import home, verify_batch
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, verify_batch, reset_admin

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('verify/<str:code>/', verify_batch),  
    path('reset-admin/', reset_admin),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)