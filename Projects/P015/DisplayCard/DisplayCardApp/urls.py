from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.retrieve_view),
    path('card/', views.card_view),
]
