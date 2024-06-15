from django.urls import path
from . import views
urlpatterns = [
    path('form/', views.employee_view,name="formdetails"),
    # path('emp_process/',views.employee_process_view,name='emp_process')
]