# Crate a django project, inside this project create 3 application named as EduApp, CriApp, PoliApp to get all the information about this fields with application level url.
- It is highly recommended to define url pattern in application level.
- Dont define all the url pattern for all application inisde poject level.
- For each application create seperate urls.py file and configure it.

>Note :: By defaut urls.py is avaible in project level, it is not avaiable in application level so we have to create urls.py file manually.

## Steps to create the project
1. Create a folder named as P003 
  ``` mkdir P005 ```
2. Create django project inside that folder 
    ``` django-admin startproject NewsProject ```
3. Enter to the project folder now
 ``` cd NewsProject```
4. Create the applications named as EducationApp, CricektApp, PoliticsApp .
- First app: ``` python manage.py startapp EduApp ```
- Second app: ``` python manage.py startapp CriApp ```
- Third app: ``` python manage.py startapp  PoliApp ```

5. Install all 3 apps inside settings.py file of main project.(Django dont know about our application, so we have to installed it inside settings.py file.)

)
> NewsProject/NewsProject/settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'EduApp',
    'CriApp',
    'PoliApp',
]
```
6. Define view function for EducationApp
> NewsProject/EduApp/views.py

```
from django.shortcuts import render,HttpResponse

def education_view(request):
    return HttpResponse('<h1>This is educationl app with application level url</h1>')

```
7.create urls.py file in application level(EduApp) and configure application level url
> NewsProject/EduApp/urls.py

```
from django.urls import path
from . import views
urlpatterns = [
    path('edu/',views.education_view)
]

```
8. Configure project level url
> NewsProject/NewsProject/urls.py

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EduApp/',include('EduApp.urls'))
]
```
9.Define view function for CriApp
> NewsProject/CriApp/views.py
```
from django.shortcuts import render,HttpResponse

def cricket_view(request):
    return HttpResponse('<h1>This is cricket app with application level url</h1>')

```
10.create urls.py file in application level(CriApp) and configure application level url
> NewsProject/CriApp/urls.py
```
from django.urls import path
from . import views
urlpatterns = [
    path('cri/',views.cricket_view)
]
```

11.  Configure project level url
> NewsProject/NewsProject/urls.py

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EduApp/',include('EduApp.urls')),
    path('CriApp/',include('CriApp.urls'))
]
```
12.Define view function for PoliApp
> NewsProject/PoliApp/views.py
```
from django.shortcuts import render,HttpResponse

def politics_view(request):
    return HttpResponse('<h2>This is Politics app with application level url</h2>')

```
13.create urls.py file in application level(PoliApp) and configure application level url
> NewsProject/PoliApp/urls.py
```
from django.urls import path
from . import views
urlpatterns = [
    path('poli/',views.politics_view)
]
```

14.  Configure project level url
> NewsProject/NewsProject/urls.py

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EduApp/',include('EduApp.urls')),
    path('CriApp/',include('CriApp.urls')),
    path('PoliApp/',include('PoliApp.urls')),
]

``` 

15.Run the server and send HttpRequest
```
http://127.0.0.1:8000/EduApp/edu/
http://127.0.0.1:8000/PoliApp/poli/
http://127.0.0.1:8000/CriApp/cri/

```