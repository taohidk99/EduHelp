from django.urls import path
from . import views  

urlpatterns = [
    path('add/', views.add_course, name='add_course'),  
    path('update/<int:course_id>/', views.update_course, name='update_course'),  
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),  
]