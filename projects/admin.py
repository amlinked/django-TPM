from django.contrib import admin
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models
# Register your models here.



@admin.register(models.Category)
class AdminCateg(admin.ModelAdmin):
    list_display = [ 'id' ,'name' ]
    list_per_page = 20

    
@admin.register(models.Project)
class AdminProject(admin.ModelAdmin):
    list_display = ['id' , 'category' , 'title' , 'status' , 'created_at' , 'updated_at' , 'user' , 'tasks_count']
    list_select_related = ['user' , 'category']
    list_per_page = 20
    list_editable = ['status']
    
    #انشاء دالة tasks_count , وتقليل عدد الاستعلامات
    
    def get_queryset(self, request) :
        query =  super().get_queryset(request)
        return query.annotate(_tasks_count=Count('task'))
    
    # @admin.display(description='Tasks Count')
    def tasks_count(self , obj):
        return obj._tasks_count


@admin.register(models.Task)
class AdminTask(admin.ModelAdmin):
    list_display = [ 'id' , 'description' , 'is_complated' , 'project' ]
    list_select_related = ['project']
    list_per_page = 20
    list_editable = ['is_complated']



