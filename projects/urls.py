from django.urls import path , include
from . import views
urlpatterns = [
   path('create/' , views.ProjectCreateView.as_view() , name= 'project_create') ,
   path('update/<int:pk>/' , views.ProjectUpdateView.as_view() , name= 'project_update') ,
   path('delete/<int:pk>' , views.ProjectDeleteView.as_view() , name= 'project_delete') ,

   path('task_create/' , views.TaskCreateView.as_view() , name= 'task_create') ,
   path('task_update/<int:pk>' , views.TaskUpdateView.as_view() , name= 'task_update') ,
   path('task_delete/<int:pk>' , views.TaskDeleteView.as_view() , name= 'task_delete') ,
   
   
   path('',views.ProjectListView.as_view(), name='project_list'),
]
