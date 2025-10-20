from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm , self).__init__(*args, **kwargs)
        
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
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