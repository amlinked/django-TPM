from django import forms
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm , UserChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm , self).__init__(*args, **kwargs)
        
    username = forms.CharField(
        label=_('Username'),
        max_length=80,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your username'),
            'autofocus': True,
        })
    )
    
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your password'),
            'autocomplete': 'current-password',
        })
    )

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label=_('First name'),
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your first name'),
        })
    )    
  
    last_name = forms.CharField(
            label=_('Last name'),
            max_length=30,
            required=False,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter your last name'),
            })
        )
         
    username = forms.CharField(
        label=_('Username'),
        max_length=80,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your username'),
            'autofocus': True,
        })
    )
    
    email = forms.EmailField(
        label=_('Email'),
        max_length=80,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your Email'),
            'autofocus': True,
        })
    )
    
    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your password'),
            'autocomplete': 'new-password',
        })
    )

    password2 = forms.CharField(
        label=_('Confirm Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Confirm your password'),
            'autocomplete': 'new-password',
        })
    )
        
    class Meta(UserCreationForm.Meta): # type: ignore
        
        fields = ['first_name', 'last_name', 'username', 'email']    
        
        
class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Username'),
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('First Name'),
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Last Name'),
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Email Address'),
            }),
        }
        
        labels = {
            'username': _('Username'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email'),
        } 
        