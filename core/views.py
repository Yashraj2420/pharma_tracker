from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Batch, Shipment
from datetime import date

def home(request):
    code = request.GET.get('code')

    if code:
        return verify_batch(request, code)

    return render(request, 'core/home.html')


def verify_batch(request, code):
    try:
        batch = Batch.objects.get(batch_code=code.strip())

        is_expired = batch.exp_date < date.today()
        shipment = Shipment.objects.filter(batch=batch).last()

        return render(request, 'core/verify.html', {
            'batch': batch,
            'valid': True,
            'expired': is_expired,
            'shipment': shipment
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

def seed_demo_data(request):
    from datetime import date

    data = [
        {
            "name": "Paracetamol 500mg",
            "manufacturer": "Cipla",
            "description": "Used for fever, headache, and mild body pain relief.",
            "batch_code": "PCM500B001",
            "mfg_date": date(2024, 1, 10),
            "exp_date": date(2028, 1, 10),
            "quantity": 1000,
            "from_location": "Mumbai Plant",
            "to_location": "Delhi Distributor",
            "status": "In Transit",
        },
        {
            "name": "Azithromycin 250mg",
            "manufacturer": "Sun Pharma",
            "description": "Antibiotic used to treat bacterial infections.",
            "batch_code": "AZM250B002",
            "mfg_date": date(2024, 2, 15),
            "exp_date": date(2028, 10, 15),
            "quantity": 800,
            "from_location": "Gujarat Plant",
            "to_location": "Lucknow Distributor",
            "status": "Dispatched",
        },
        {
            "name": "Amoxicillin 500mg",
            "manufacturer": "Dr. Reddy's",
            "description": "Broad-spectrum antibiotic used for bacterial infections.",
            "batch_code": "AMX500B003",
            "mfg_date": date(2024, 3, 12),
            "exp_date": date(2028, 8, 20),
            "quantity": 1200,
            "from_location": "Hyderabad Plant",
            "to_location": "Noida Warehouse",
            "status": "Delivered",
        },
        {
            "name": "Pantoprazole 40mg",
            "manufacturer": "Lupin",
            "description": "Reduces stomach acid and treats acidity.",
            "batch_code": "PAN40B005",
            "mfg_date": date(2024, 4, 5),
            "exp_date": date(2029, 1, 31),
            "quantity": 950,
            "from_location": "Goa Plant",
            "to_location": "Delhi Medical Store",
            "status": "In Transit",
        },
        {
            "name": "Metformin 500mg",
            "manufacturer": "Abbott",
            "description": "Used to control blood sugar levels.",
            "batch_code": "MET500B006",
            "mfg_date": date(2024, 2, 28),
            "exp_date": date(2028, 11, 30),
            "quantity": 1500,
            "from_location": "Ahmedabad Plant",
            "to_location": "Gurgaon Distributor",
            "status": "Delivered",
        },
        {
            "name": "Dolo 650",
            "manufacturer": "Micro Labs",
            "description": "Used for fever and pain relief.",
            "batch_code": "DOL650B007",
            "mfg_date": date(2024, 5, 1),
            "exp_date": date(2029, 6, 30),
            "quantity": 1100,
            "from_location": "Bengaluru Plant",
            "to_location": "Jaipur Distributor",
            "status": "Dispatched",
        },
    ]

    for item in data:
        product, created = Product.objects.get_or_create(
            name=item["name"],
            defaults={
                "manufacturer": item["manufacturer"],
                "description": item["description"],
            }
        )

        batch, created = Batch.objects.get_or_create(
            batch_code=item["batch_code"],
            defaults={
                "product": product,
                "mfg_date": item["mfg_date"],
                "exp_date": item["exp_date"],
                "quantity": item["quantity"],
            }
        )

        Shipment.objects.get_or_create(
    from_location=item["from_location"],
    to_location=item["to_location"],
    status=f'{item["batch_code"]} - {item["status"]}',
)
        

    return HttpResponse("Demo products, batches, and shipments restored successfully.")