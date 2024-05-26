
from django.urls import path
from . import views
urlpatterns = [
    path('shirts/',views.retrieve_view),
    
]
