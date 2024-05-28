from django.urls import path
from . import views

urlpatterns = [
    path('wish/<str:name>/',views.wish_view),
    path('add/<int:a>/<int:b>/',views.add_view),
]