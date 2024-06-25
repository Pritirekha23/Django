from django.urls import path
from . import views

urlpatterns = [
    path('chai/',views.all_chai,name='chai'),
    path('order/',views.order_view,name='order'),
    path('chai_store/',views.chai_store_view,name='chai_store'),
]
