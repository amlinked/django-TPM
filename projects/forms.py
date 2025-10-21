from django import forms
from . import models
from django.utils.translation import gettext_lazy as _

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category' ,'title' , 'description' ]
        widgets = {
            'category' : forms.Select(attrs={'class': 'form-select'}),
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' :forms.Textarea(attrs={'class': 'form-control', 'rows': 6})
        }
        
class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category' ,'title' , 'description' , 'status' ]
        widgets = {
            'category' : forms.Select(attrs={'class': 'form-select'}),
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' :forms.Textarea(attrs={'class': 'form-control'}),
            'status' : forms.Select(attrs={'class': 'form-select'})
            
        }        
        labels = {
            'category': _('Category'),
            'title': _('Title'),
            'description': _('Description'),
            'status': _('Status'),
        } 