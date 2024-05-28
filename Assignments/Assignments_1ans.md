# Django Framework

### Assignments: 1

- 1. What motivated Adrian Holovaty and Simon Willison to create Django?
     > Adrian Holovaty and Simon Willison created Django while working at the Lawrence Journal-World newspaper. They developed the framework to create complex news websites and web applications quickly and easily. The name "Django" comes from the guitarist Django Reinhardt, and the first version of Django was released to the public in 2005, making it an open-source framework. The motivation behind creating Django was to simplify the process of web development and make it more accessible to developers, especially those who were new to web development or who wanted to build web applications quickly without sacrificing quality.
- 2. When was Django first released as an open-source project?
     > Django was released to the public on July 21, 2005

- 3. What is the inspiration behind the name "Django"?
     > Adrian Holovaty and Simon Willison are then fan of Jean Reinhardt known by his Romani nickname Django . so when they created this new framework they give this name.
- 4. Which package manager do you typically use to install Django?
     > pip package manager

- 5. How do you install Django using pip?
     > pip install django

- 6. What is the command to install a specific version of Django using pip ?

> pip install django=5.0.2

- 7. Apart from pip, are there any other methods to install Django?
     >

- 8. How do you display the Django version you are using ?
     > django-admin --version
- 9. How can you check if Django is already installed on your system ?
     > we can check the django version if django is available then it will show the version else it will raise an error.

- 10. What command is used to upgrade Django to the latest version using pip ?
      > pip install --upgrade django

- 11. What distinguishes Django from other web frameworks of its time?
      > Its features slike Ridiculously fast Fully loaded,Reassuringly secure,Highly scalable,Incredibly versatile,Rapid Development,Batteries-Included Philosophy,Built-in Admin Interface,Template Engine,ORM (Object-Relational Mapping),REST Framework,Community Support,Documentation distinguishes Django from other web frameworks.

- 12. How did Django gain popularity and widespread adoption after its initial release?
      >

- 13. Who currently maintains and oversees the development of Django?
      > The DSF (Django Software Foundation) maintains Django.

- 14. Briefly describe the purpose of a model in a Django application.
      > In Django, a model is the database layer where all the database codes are present.

- 15. What is the difference between a URL and a view in Django?
      > In django URL defines the path to go to the website or specific page of the website but views is the Business layer where we write our programs in python language.
      > URL : Acts as a route or a mapping from a web address to a view.,Defined in urls.py.,Directs incoming HTTP requests to the appropriate view
      > Contains the logic for handling a request and returning a response.,Defined in views.py.,Processes the request, interacts with the database (if needed), and returns an HTTP response (e.g., rendering a template, returning JSON data).

- 16. How do you include static files (images, CSS, JavaScript) in your Django templates?
      > create images, CSS, JavaScript folders inside templates folder and make the configurations for it.

- 17. How do you run the Django development server with other port number like 7070.
      > python manage.py runserver 8005
      > url : http://127.0.0.1:8005/

- 18. Where do you typically store static files in a Django project?
      > In Django project static files are stored in main project the path will be like : ProjectName/static/file_name
      > Inside App_name create corresponding folders and inside that folder create specific file to store.(ex: ProjectName/static/App_name/css/style.css)
      > StaticProject/static/css/style.css
- 19. Where do you store template files in a Django project.
      > In Django project templates files are stored in main project the path will be like : ProjectName/templates/App_name(This app name is not created using django command this is the corresponding django app name to store specific templates according to that mainapp, we createed this because one project may have many appps)/file_name
      > TemplateTagProject/templates/TemplateTagApp/time.html)
- 20. How do you add a new app to your Django project?
      > After creating the app using py manage.py startapp we have to install it inside setting.py file.
      > ex:

```
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'StaticApp',
]

```

- 21. Write a Django view that fetches all Product objects from the database and renders them in a template.
      >

  ```
from django.shortcuts import render
from .models import Shirts

# Create your views here.
def retrieve_view(request):
    records=Shirts.objects.all()
    d={
        'records':records
    }
    return render(request,'DisplayRecordsApp/Shirts.html',d)

templates/Shirts.html
 {% for i in records %}
      <tr>
        <td>{{i.id}}</td>
        <td>{{i.brand}}</td>
        <td>{{i.price}}</td>
        <td>{{i.color}}</td>
      </tr>
{% endfor %}
     ```

- 22. Write the template tag to load static files.
      > Loading the static template tag: {% load static %}
- 23. Write the code to reference a CSS file styles.css located in the static directory.
      ```<link rel="stylesheet" href="{% static 'css/styles.css' %}">```

- 24. How do you apply migrations in Django?
      > By using command : py manage.py makemigrations and then to execute it use command: py manage.py migrate

- 25. How do you create a superuser in Django?
      > By using command : py manage.py createsuperuse and then provide userid,email and password

- 26. How do you configure the location of static files in settings.py?

```
STATIC_URL = 'static/'
STATIC_DIR=BASE_DIR/'static'
STATICFILES_DIRS=[STATIC_DIR,]

```

- 27. How do you pass context data to a Django template?
      > Inside views.py file store data in dictionary format and send that contest dictionary using render function, then use template variavle to show that data <h2>Current time is : {{ time}} </h2> .

```
from django.shortcuts import render
from datetime import datetime

def time_view(request):
    current_date_time=datetime.now()
    time=current_date_time.strftime('%H:%M:%S')
    d={'time':time}
    return render(request,'TemplateTagApp/time.html/',d)
``
- 28. How do you access a variable name passed from the view in a Django template?
> Using template variable,
```

syntax : {{template_variable}}

```
- 29. How do you retrieve  all objects of a model in Django?
>     Student= Students.objects.all()

- 30. How do you map a URL to a view in Django?
> step1: create view
```

# TemplateProject/TemplateApp/views.py

from django.shortcuts import render

def odisha_view(request):
return render(request,'TemplateApp/odisha.html')

```
> step2:  project url(Include App URLs in Project URLs)
```

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
path('admin/', admin.site.urls),
path('TemplateApp/',include('TemplateApp.urls'))
]

```
> step3:  app url
```

from django.urls import path
from . import views

urlpatterns = [
path('odisha/', views.odisha_view),

]

```
- 31. How do you include URLs from an app in the project's main urls.py?
> To include URLs from an app in the project's main urls.py file, you need to use the include() function from django.urls. This function allows you to reference the urls.py file of an app, effectively including its URL patterns in the project's main URL configuration.
```

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
path('admin/', admin.site.urls),
path('TemplateApp/',include('TemplateApp.urls'))
]

```
- 32. Write a model method to return the name of a student object.
>
```

from django.db import models

class Student(models.Model):
name = models.CharField(max_length=30)

    def __str__(self):
       return self.name

```
- 33. Write a simple view to render  a template called  home.html.

```

# SimpleProject/SimpleApp/views.py

from django.shortcuts import render

def home_view(request):
return render(request,'SimpleApp/home.html')

```
- 34. Map a URL pattern to the home view.
>  define the urlpattern in app level: Assignments/PA001/SimpleProject/SimpleApp/views.py
```

from django.urls import path
from . import views

urlpatterns = [
path('home/', views.home_view),
]

```

> create home_view in views.py file
```

from django.shortcuts import render

def home_view(request):
return render(request,'SimpleApp/home.html')

```


- 35. How do you perform a for loop over a list called  l in a Django template?

```

{% for i in l %}
   {{ i }}
{% endfor %}

```
- 36. How do you register a model with the Django admin site?
> we can register a model with django in two ways
```

# 1st way

from django.contrib import admin
from .models import Electronics
admin.site.register(Electronics)

# 2nd way

from django.contrib import admin
from .models import Mobile

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
list_display=('id','name','brand','price')

```
- 37. How do you capture a variable from a URL pattern and pass it to a view ?
```

> CapturedParameters/CapturedParametersApp/urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('wish/<str:name>/',views.wish_view),
    path('add/<int:a>/<int:b>/',views.add_view),
]
```

> CapturedParameters/CapturedParametersApp/views.py

```
from django.shortcuts import render
def wish_view(request,name):
    d={ 'name':name}
    return render(request,'CapturedParametersApp/wish.html',d)
def add_view(request,a,b):
    add=a+b
    d={'add':add}
    return render(request,'CapturedParametersApp/add.html',d)
```
