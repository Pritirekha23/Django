from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.education_form_view,name="education"),
    path('personal/',views.personal_form_view,name="personal"),
    path('extracur/',views.extra_cur_form_view,name="extracur"),
    path('data/',views.data_view,name="data"),
   
]