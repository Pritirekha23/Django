from django.shortcuts import render
from datetime import datetime

# Create your views here.
def wish_view(request,name):
    current_date_time=datetime.now()
    time=int(current_date_time.strftime('%H'))
    if time>=4 and time<12:
        wish='Good Morning'
    elif time>=12 and time<17:
        wish='Good Afternoon'
    elif time>=17 and time<22:
        wish='Good evening'
    else:
        wish='Good Night'
    d={'time':time,'wish':wish, 'name':name}
    return render(request,'CapturedParametersApp/wish.html',d)

def add_view(request,a,b):
    add=a+b
    d={'add':add}
    return render(request,'CapturedParametersApp/add.html',d)

