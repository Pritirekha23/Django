from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('signup/',views.signup_view,name="signup"),
    path('success/',views.success_view,name="success"),
    path('signin/',views.signin_view,name="signin"),
    path('dashboard/',views.dashboard_view,name="dashboard"),
]