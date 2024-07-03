from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view,name="home"),
    path('add_task/',views.add_task_view,name="add_task"),
    path('done_task/<int:id>',views.done_task_view,name="done_task"),
    path('undo_task/<int:id>',views.undo_task_view,name="undo_task"),
    path('delete_task/<int:id>',views.delete_task_view,name="delete_task"),
    path('delete_all/',views.delete_all_view,name="delete_all"),
    path('clear_all/',views.clear_all_view,name="clear_all"),
    path('remove_all/',views.remove_all_view,name="remove_all"),
]
