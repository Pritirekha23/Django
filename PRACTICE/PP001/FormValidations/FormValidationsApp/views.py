from django.shortcuts import render


def all_chai(request):
    return render(request,'FormValidationsApp/all_chai.html')

def order_view(request):
    return render(request,'FormValidationsApp/order.html')

def chai_store_view(request):
    return render(request,'FormValidationsApp/chai_store.html')
