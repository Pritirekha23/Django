
```
P:\Fullstack_django\Backend_learnings\Django\Minor_Projects\MP003> django-admin startproject TaskManagementSystem 
P:\Fullstack_django\Backend_learnings\Django\Minor_Projects\MP003> cd .\TaskManagementSystem\
P:\Fullstack_django\Backend_learnings\Django\Minor_Projects\MP003\TaskManagementSystem> py manage.py startapp Tmsapp
P:\Fullstack_django\Backend_learnings\Django\Minor_Projects\MP003\TaskManagementSystem>mkdir templates
P:\Fullstack_django\Backend_learnings\Django\Minor_Projects\MP003\TaskManagementSystem>cd templates
P:\Fullstack_django\Backend_learnings\Django\Minor_Projects\MP003\TaskManagementSystem\templates>mkdir Tmsapp
```
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Tmsapp',
]

 'DIRS': [BASE_DIR/'templates'],


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'UNIVERSITY',
        'USER':'root',
        'PASSWORD':'root_db',
    }
}

```