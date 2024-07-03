from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('courses/',views.courses_view,name='courses'),
    path('trainers/',views.trainers_view,name='trainers'),
    path('blogs/',views.blogs_view,name='blogs'),
    path('aboutus/',views.aboutus_view,name='aboutus'),
    path('contactus/',views.contactus_view,name='contactus'),
]
