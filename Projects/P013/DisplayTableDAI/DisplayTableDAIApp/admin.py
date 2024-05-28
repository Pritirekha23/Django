from django.contrib import admin
from .models import Mobile
# Register your models here.

# oneway
# class MobileAdmin(admin.ModelAdmin):
#     list_display=('id','name','brand','price')

# admin.site.register(Mobile,MobileAdmin)

#by using decorator
@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display=('id','name','brand','price')

