from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view,name="home_records"),
    path('specfic_country_record/<int:id>',views.specfic_country_record,name='specfic_country_record')
]