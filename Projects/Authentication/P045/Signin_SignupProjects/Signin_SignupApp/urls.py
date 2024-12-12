from . import views
from django.urls import path

urlpatterns = [
    path('redg_form/', views.redg_view),
    path('signin/',views.signin_view,name='signin'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('signout/',views.signout_view,name='signout'),
]
