from django.shortcuts import render, HttpResponse,redirect
from .forms import AddProductForm

def home_view(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['Product_Name']
            quantity = form.cleaned_data['Quantity']
            product_name = product_name.replace(' ', '-')
            response = redirect('home')
            response.set_cookie(product_name,quantity)
    else:
        form = AddProductForm()
        context = {'form': form}
        return render(request, 'AddProductApp/home.html', context)
    return response

def display_view(request):
    all_records = request.COOKIES 
    return render(request, 'AddProductApp/display.html', {'all_records': all_records})
