from django.urls import path
from . import views

urlpatterns = [
    path('home_records/',views.home_view,name='home_records'),
    path('profile_pic_records/<int:id>',views.profile_details_view,name='profile_pic_records'),   
] 