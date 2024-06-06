from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.retrieve_view,name='all_records'),
    path('specific_card/<int:id>', views.card_view,name='specific_card'),
]
