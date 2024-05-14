from django.urls import path
from . import views

urlpatterns = [
    path('odisha/', views.odisha_view),
    
]
