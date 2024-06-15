from django.urls import path
from . import views
urlpatterns = [
    path('form/', views.employee_view,name="formdetails"),
]