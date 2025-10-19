from django import forms
from . import models

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