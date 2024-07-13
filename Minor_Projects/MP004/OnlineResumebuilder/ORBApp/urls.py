from django.urls import path
from . import views

urlpatterns = [
    path('',views.info,name='info'),
    path('all_resume_view/',views.all_resume_view,name='all_resume_view'),
    path('resume/<int:id>/', views.resume_view, name='resume'),

] 
