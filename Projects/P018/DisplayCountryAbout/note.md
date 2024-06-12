
### Step-1
- create project and application
```
PS P:\Fullstack_django\Backend_learnings\Django\Projects\P017> django-admin startproject Country
PS P:\Fullstack_django\Backend_learnings\Django\Projects\P017> cd .\Country\
PS P:\Fullstack_django\Backend_learnings\Django\Projects\P017\Country> py manage.py startapp CountryApp

```
### Step-2
- Install the application inside settings.py file
>DisplayCountryAbout/DisplayCountryAbout/settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DisplayCountryAboutApp',
]
```

### Step-3
- create templates folder in main project level inside templates folder cretae the corresponding app folder and inside that create home.html and description.html files.
>DisplayCountryAbout/templates/DisplayCountryAboutApp/home.html , DisplayCountryAbout/templates/DisplayCountryAboutApp/description.html

### Step-4
-configure the templates folder in settings.py file.
>DisplayCountryAbout/DisplayCountryAbout/settings.py

```
'DIRS': [BASE_DIR/'templates'],
```
<!-- STATIC_URL = 'static/'
STATIC_DIR=BASE_DIR/'static'
STATICFILES_DIRS=[STATIC_DIR,] -->

### Step-5
- project level url
>DisplayCountryAbout/DisplayCountryAbout/urls.py
```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('DisplayCountryAboutApp/',include('DisplayCountryAboutApp.urls'))
]
```
### Step-6
- Application level url (create urls.py inside application )
>DisplayCountryAbout/DisplayCountryAboutApp/urls.py
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
>DisplayCountryAbout/DisplayCountryAboutApp/views.py
```
from django.shortcuts import render
from .models import Country

def home_view(request):
    all_records=Country.objects.all()
    d={'all_records':all_records}
    return render(request,'DisplayCountryABoutApp/home.html',d)

def specfic_country_record(request,id):
    records=Country.objects.get(id=id)
    d={'records':records}
    return render(request,'DisplayCountryABoutApp/description.html',d)
```


### Step-8
- configure database inside setting.py
>DisplayCountryAbout/DisplayCountryAbout/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'PRODUCTS',
        'USER':'root',
        'PASSWORD':'root_db',
    }
}
```

### Step-9
- create the model and migrate it
>DisplayCountryAbout/DisplayCountryAboutApp/models.py
```
from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=50)
    capital_name = models.CharField(max_length=50)
    population = models.PositiveIntegerField()
    heading = models.CharField(max_length=200)
    readmore = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.country_name
```

> py manage.py makemigrations
> py manage.py migrate 


### Step-10
-  register the admin.
>DisplayCountryAbout/DisplayCountryAboutApp/admin.py
```
from django.contrib import admin
from .models import Country

admin.site.register(Country)
```

### Step-11
-  create superuser and login to the Django Admin Interface then insert data to the data base.
```
py manage.py createsuperuser
Username (leave blank to use 'asus'): priti2002
Email address: 
Password: priti2006
Password (again):priti2006
Superuser created successfully.
```

### Step-12
-  views file
>DisplayCountryAbout/DisplayCountryAboutApp/views.py
```
from django.shortcuts import render
from .models import Country

def home_view(request):
    all_records=Country.objects.all()
    d={'all_records':all_records}
    return render(request,'DisplayCountryABoutApp/home.html',d)

def specfic_country_record(request,id):
    records=Country.objects.get(id=id)
    d={'records':records}
    return render(request,'DisplayCountryABoutApp/description.html',d)
```

### Step-13
- templates file
>DisplayCountryAbout/templates/DisplayCountryAboutApp/home.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>DisplayCountryAboutApp project</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />

    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.10.0/font/bootstrap-icons.min.css">
  </head>
  <body class="bodyhome">
    <div class="container m-4 rounded p-4" >
        <h1 class="text-center">Country Records</h1>
        <table class="table border border-warning "  >
          <thead>
            <tr>
              <th scope="col"> ID</th>
              <th scope="col"> country_name</th>
              <th scope="col"> capital_name</th>
              <th scope="col"> population  </th>
              <th scope="col"> Readmore  </th>
            </tr>
          </thead>
          <tbody>
            {% for i in all_records %}
            <tr class="records_td" >
              <td>{{i.id}}</td>
              <td>{{i.country_name}}</td>
              <td>{{i.capital_name}}</td>
              <td>{{i.population}}</td>
              <td><a class="btn btn-danger" href="{% url 'specfic_country_record' i.id %}">{{i.readmore}}  <i class="bi bi-arrow-right"></i></a></td>
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
>DisplayCountryAbout/templates/DisplayCountryAboutApp/description.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />    <title>DisplayCountryAbout project</title>
    <link rel="stylesheet" href="{% static 'css/style.css'%}"/>

    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
  </head>

  <body>
    <div class="container">
      <div class="row  m-4">
        <div class="col-md-4">
          <div class="card p-3 mb-2 bg-secondary text-white" style="width: 50rem; ">
            <div class="card-body ">
              <h4 class="text-center text-warning"><u>{{records.heading}}</u></h4>
              {% comment %} <h5 class="card-title text-cente">Id: {{records.id}}</h5> {% endcomment %}
             <div class="flexcc">
                <p class="card-text"><b>Capital:</b>
                  <i> <b class="text-infoo">{{records.capital_name}} </b></i>
                </p>
                <p class="card-text "><b>Population:</b>
                  <i> <b class="text-infoo">{{records.population}}  </b></i>
                </p>
             </div> 

              <p class="card-text"> {{records.description}}</p>\

              <div class="text-center" id="btn">
                <a  href="{% url 'home_records' %}" class="btn btn-danger">Back to Home</a>
              </div>
              
            </div>
          </div>
      </div>
   </div>


    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### Step-15
- run server and send http request.

```
py manage.py runserver

home: http://127.0.0.1:8000/DisplayCountryAboutApp/home/
specific country details: http://127.0.0.1:8000/DisplayCountryAboutApp/specfic_country_record/1


```
