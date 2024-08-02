
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home" ),
    path('display/',views.display_view,name="display"),
   
]