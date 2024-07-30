from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.education_form_view,name="education"),
    path('personal/',views.personal_form_view,name="personal"),
    path('extracur/',views.extra_cur_form_view,name="extracur"),
    path('data/',views.data_view,name="data"),
   
]
#  <h3>{{all_records.name}}</h3>
#         <p>Address: {{all_records.address}}</p>
#         <p>Email: {{all_records.email}}</p>
#         <p>College: {{all_records.college}}</p>
#         <p>Degree: {{all_records.degree}}</p>
#         <p>Mark: {{all_records.mark}}</p>
#         <p>Favorite Sports: {{all_records.fav_sports}}</p>
#         <p>Favorite Actor: {{all_records.actor}}</p>