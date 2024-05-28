from django.shortcuts import render
from .models import Shirts

# Create your views here.
def retrieve_view(request):
    records=Shirts.objects.all()
    d={
        'records':records
    }
    return render(request,'DisplayRecordsApp/Shirts.html',d)
