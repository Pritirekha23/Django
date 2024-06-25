from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.employee_view,name='employee_view'),
    path('display_records/',views.display_records,name="display_records"),
]
