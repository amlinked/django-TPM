from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy  , reverse
from . import models
from. import forms
# Create your views here.

class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'
    
class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html' 
    
    success_url = reverse_lazy('project_list')
    
class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html' 
    
    def get_success_url(self) :
        return reverse('project_update' , args=[self.object.id]) # type: ignore
 
class ProjectDeleteView(DeleteView):
    model = models.Project
    # template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')
    
       
class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project','description' , 'is_complated']
    http_method_names=  ['post']
    # template_name = 'project/taskcreate.html' 
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id]) # type: ignore
    
class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_complated']
    http_method_names=  ['post']
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id]) # type: ignore  
    
class TaskDeleteView(DeleteView):
    model = models.Task
    http_method_names=  ['post']
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id]) # type: ignore      