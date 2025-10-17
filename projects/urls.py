from django.urls import path , include
from . import views
urlpatterns = [
   path('create/' , views.ProjectCreateView.as_view() , name= 'project_create') ,
   path('home/',views.ProjectListView.as_view(), name='project_list'),
]
