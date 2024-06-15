from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Calculator_view,name='home'),
    
]
