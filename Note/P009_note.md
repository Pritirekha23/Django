# Static files in Django 
> DATE 17/05/2024

- Sometime we required images, videos, audios, css, javascript at that time we can go for static file.
- Django by deafult does not provide any support for static files.
- We have to create and configure manually.

## How to create and configure static file
----------------------------------------
-> Create a folder named as 'static' in main project level / just like 'template' folder.
-> Inside that ststic folder create sub folders like css, javascript, image etc.
-> Django does not aware about our static folder so we have to configure inside settings.py file.
-> In .html file first load the static file.

# P007
----
### Problem Statement : Add some image, css in the django project.

All steps:

- Step 1 : Common steps
```
P:\Django\Projects\P009>django-admin startproject StaticProject 
P:\Django\Projects\P009>cd StaticProject
P:\Django\Projects\P009\StaticProject>py manage.py startapp StaticApp
then install the app in settings.py
```

- Step 2 : Create a folder named as 'static' in main project level.
- Step 3 : Create sub folder inside static folder (like css, images)
Step 4 : Configure static folder inside settings.py file.
>StaticProject/StaticProject/settings.py
```
STATIC_URL = 'static/'
STATIC_DIR=BASE_DIR/'static'
STATICFILES_DIRS=[STATIC_DIR,]
```
- Step 5 : Create templates folder in main project level and configure it inside settings.py file.
>StaticProject/StaticProject/settings.py
```
 'DIRS': [BASE_DIR,'templates'],
```
- Step 6 : Define view function .
>StaticProject/StaticApp/views.py
```
from django.shortcuts import render

def home_view(request):
    return render(request,'StaticApp/home.html')
```
- Step 7: Define project and application level url 
>Project level url : StaticProject/StaticProject/urls.py
```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StaticApp/',include('StaticApp.urls'))
]
```
>Application level url : StaticProject/StaticApp/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view),
]
```
- Step 8 :Design webpage in home.html file 
### Note : First load the static file : {% load static %}
### Note : By using jinja synatax we can add the src of an image and href of link tag. 

>StaticProject/templates/StaticApp/home.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Static file</title>
    <link rel="stylesheet" href="{% static "css/style.css" %}" />
  </head>
  <body>
    <h1>Different types of flowers</h1>
    <div class="main">
      <div class="div1">
        <img src="{% static "Images/01_ageratum.webp" %}" alt="image1">
      </div>
      <div class="div2">
        <img src="{% static "Images/02_aster.webp" %}" alt="iamge2">
      </div>
      <div class="div3">
        <img src="{% static "Images/03_bee-balm.webp" %}" alt="image3">
      </div>
      <div class="div4">
        <img src="{% static "Images/04_balloon-flower.webp" %}" alt="image4">
      </div>
      <div class="div5">
        <img src="{% static "Images/05_balsam.webp" %}" alt="image5">
      </div>
    </div>
  </body>
</html>

```
- Run server and send HTTP request
> http://127.0.0.1:8000/StaticApp/home/