from django.urls import path
from . import views

urlpatterns = [
    path('msg/',views.wish_view)
]