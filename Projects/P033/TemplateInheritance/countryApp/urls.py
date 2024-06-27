from django.urls import path
from . import views

urlpatterns = [
    path('india/',views.india_view,name='india'),
    path('usa/',views.usa_view,name='usa'),
    path('uk/',views.uk_view,name='uk'),
]