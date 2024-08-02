from django.urls import path
from . import views

urlpatterns = [
    path('count/',views.page_count_view),
]

