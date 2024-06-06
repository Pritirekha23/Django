from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAmin(admin.ModelAdmin):
    list_display=('id','country_name','capital_name','population'
    ,'Readmore')

