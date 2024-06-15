from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.Student_form_view),

]