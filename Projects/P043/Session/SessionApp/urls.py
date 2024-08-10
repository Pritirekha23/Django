from django.urls import path
from . import views

urlpatterns = [
    path('session/', views.session_view),
    path('get_session/',views.get_session_view,name="get_session"),
    path('deleted_session/',views.delete_session_view,name="deleted_Session"),
    path('page_count/',views.page_count_view,name="page_count")
]
