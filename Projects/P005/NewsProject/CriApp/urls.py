from django.urls import path
from . import views
urlpatterns = [
    path('cri/',views.cricket_view)
]