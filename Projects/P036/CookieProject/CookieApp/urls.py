from django.urls import path
from . import views

urlpatterns = [
    path('set_cookies/',views.set_cookie_view),
    path('get_cookies/',views.get_cookie_view),
    path('delete_cookies/',views.delete_cookie_view),
]
