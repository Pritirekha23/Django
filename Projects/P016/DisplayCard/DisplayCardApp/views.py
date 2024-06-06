from django.shortcuts import render
from .models import Student

# Create your views here.
def retrieve_view(request):
    all_records=Student.objects.all()
    d={
        'all_records':all_records
    }
    return render(request,'DisplayCardApp/records.html',d)

def card_view(request,id):
    record=Student.objects.get(id=id)
    d={'record':record}
    return render(request,'DisplayCardApp/card.html',d)