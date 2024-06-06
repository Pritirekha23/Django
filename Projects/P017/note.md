
### Step-1
- create project and application
```
PS P:\Fullstack_django\Backend_learnings\Django\Projects\P017> django-admin startproject Country
PS P:\Fullstack_django\Backend_learnings\Django\Projects\P017> cd .\Country\
PS P:\Fullstack_django\Backend_learnings\Django\Projects\P017\Country> py manage.py startapp CountryApp

```
### Step-2
- Install the application inside settings.py file
>Country/Country/settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CountryApp',
]
```

### Step-3
- create templates folder in main project level inside templates folder cretae the corresponding app folder and inside that create home.html and description.html files.
>Country/templates/CountryApp/home.html , Country/templates/CountryApp/description.html

### Step-4
-configure the templates folder in settings.py file.
>Country/Country/settings.py
```
'DIRS': [BASE_DIR/'templates'],
```
<!-- STATIC_URL = 'static/'
STATIC_DIR=BASE_DIR/'static'
STATICFILES_DIRS=[STATIC_DIR,] -->

### Step-5
- project level url
>Country/Country/urls.py
```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CountryApp/',include('CountryApp.urls'))
]
```
### Step-6
- Application level url (create urls.py inside application )

```
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view,name="home_records"),
    path('specfic_country_record/<int:id>',views.specfic_country_record,name='specfic_country_record')
]
```
### Step-7
- create views 
>Country/CountryApp/views.py
```
from django.shortcuts import render

def home_view(request):
    return render(request,'CountryApp/home.html')
```


### Step-8
- configure database inside setting.py
>Country/Country/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ORGANIZATION',
        'USER':'root',
        'PASSWORD':'root_db'
    }
}
```

### Step-9
- create the model and migrate it
>Country/CountryApp/models.py
```
class Country(models.Model):

    country_name=models.CharField(max_length=30)
    capital_name=models.CharField(max_length=30)
    population=models.IntegerField()
    Readmore=models.CharField(max_length=30)
```

> py manage.py makemigrations
> py manage.py migrate 


### Step-10
-  register the admin.
>Country/CountryApp/admin.py
```
from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAmin(admin.ModelAdmin):
    list_display=('id','country_name','capital_name','population','Readmore')
```

### Step-11
-  create superuser and login to the Django Admin Interface then insert data to the data base.
```
py manage.py createsuperuser
Username (leave blank to use 'asus'): dj23
Email address: 
Password: dj102423
Password (again): dj102423
Superuser created successfully.
```

### Step-12
-  views file
```
from django.shortcuts import render
from .models import Country

def home_view(request):
    all_records=Country.objects.all()
    d={'all_records':all_records}
    return render(request,'CountryApp/home.html',d)

def specfic_country_record(request,id):
    record=Country.objects.get(id=id)
    d={'record':record}
    return render(request,'CountryApp/description.html',d)
```

### Step-13
- templates file
>>Country/templates/CountryApp/home.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>DisplayCard project</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />

    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <div class="container m-4 rounded p-4" id="table-background">
        <h1 class="text-center" id="heading">Country Records</h1>
  
        <table class="table border border-warning "  >
          <thead>
            <tr>
              <th scope="col"> ID</th>
              <th scope="col"> country_name</th>
              <th scope="col"> capital_name</th>
              <th scope="col"> population  </th>
              <th scope="col"> Readmore </th>
            </tr>
          </thead>
          <tbody>
            {% for i in all_records %}
            <tr class="records_td">
              <td>{{i.id}}</td>
              <td>{{i.country_name}}</td>
              <td>{{i.capital_name}}</td>
              <td>{{i.population}}</td>
              <td><a href="{% url 'specfic_country_record' i.id %}">{{i.Readmore}}</a></td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### Step-14
- templates file
>>Country/templates/CountryApp/description.html
```

```