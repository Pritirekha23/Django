from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EducationForm, PersonalForm, ExtracurForm

def education_form_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            response = HttpResponse(render(request, 'StudentInfoApp/personal_form.html', {'form': PersonalForm()}))
            response.set_cookie('college', form.cleaned_data['college'])
            response.set_cookie('degree', form.cleaned_data['degree'])
            response.set_cookie('mark', form.cleaned_data['mark'])
            return response
    else:
        form = EducationForm()
    
    return render(request, 'StudentInfoApp/education_form.html', {'form': form})

def personal_form_view(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            response = HttpResponse(render(request, 'StudentInfoApp/extra_cur.html', {'form': ExtracurForm()}))
            response.set_cookie('name', form.cleaned_data['name'])
            response.set_cookie('address', form.cleaned_data['address'])
            response.set_cookie('email', form.cleaned_data['email'])
            return response
    else:
        form = PersonalForm()
    
    return render(request, 'StudentInfoApp/personal_form.html', {'form': form})

def extra_cur_form_view(request):
    if request.method == 'POST':
        form = ExtracurForm(request.POST)
        if form.is_valid():
            response = HttpResponse(render(request, 'StudentInfoApp/extra_cur.html', {'form': form}))
            response.set_cookie('fav_actor', form.cleaned_data['fav_actor'])
            response.set_cookie('fav_flower', form.cleaned_data['fav_flower'])
            return response
    else:
        form = ExtracurForm()
    
    return render(request, 'StudentInfoApp/extra_cur.html', {'form': form})



def data_view(request):
    all_records = {
        'name': request.COOKIES.get('name'),
        'address': request.COOKIES.get('address'),
        'email': request.COOKIES.get('email'),
        'college': request.COOKIES.get('college'),
        'degree': request.COOKIES.get('degree'),
        'mark': request.COOKIES.get('mark'),
        'fav_actor': request.COOKIES.get('fav_actor'),
        'fav_flower': request.COOKIES.get('fav_flower')
    }
    return render(request, 'StudentInfoApp/data.html', {'all_records':all_records})