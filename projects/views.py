from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.urls import reverse_lazy  , reverse
from django.db.models import Q

from . import models
from. import forms
# Create your views here.

class ProjectListView(LoginRequiredMixin , ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        return queryset
    
class ProjectCreateView(LoginRequiredMixin , CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html' 
    
    success_url = reverse_lazy('project_list')
    
    def form_valid(self , form):
        form.instance.user  = self.request.user
        return super().form_valid(form)
    
class ProjectUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html' 
    
    def get_success_url(self) :
        return reverse('project_update' , args=[self.object.id]) # type: ignore
    
    def test_func(self):
        update = self.get_object()
        return update.user == self.request.user # type: ignore

 
class ProjectDeleteView(LoginRequiredMixin , UserPassesTestMixin ,DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')
    
    def test_func(self):
        update = self.get_object()
        return update.user == self.request.user # type: ignore
       
class TaskCreateView(LoginRequiredMixin , UserPassesTestMixin, CreateView):
    model = models.Task
    fields = ['project','description' , 'is_complated']
    http_method_names=  ['post']
    # template_name = 'project/taskcreate.html' 
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id]) # type: ignore
    
    def test_func(self):
        project_id = self.request.POST.get('project')
        if project_id:
            project = get_object_or_404(models.Project, pk=project_id)
            return project.user == self.request.user
        return False
    
class TaskUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = models.Task
    fields = ['is_complated']
    http_method_names=  ['post']
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id]) # type: ignore  
    
    def test_func(self):
        task = self.get_object()
        return task.project.user == self.request.user  # type: ignore
    
class TaskDeleteView(LoginRequiredMixin ,UserPassesTestMixin , DeleteView):
    model = models.Task
    http_method_names=  ['post']
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id]) # type: ignore     
    
    def test_func(self):
        task = self.get_object()
        return task.project.user == self.request.user  # type: ignore