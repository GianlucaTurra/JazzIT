from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import MusicAdvice


INPUT_CLASSES = 'border border-extra text-main rounded-lg block w-full'


class LoginForm(AuthenticationForm):
    """Django Form for user login

    Form input fields are defined here wile labels and input button are in the template
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': INPUT_CLASSES
    }))


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': _('Your username')}), 
        label=_('Username'),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': INPUT_CLASSES, 'placeholder': _('Enter your email')}), 
        label=_('Email'),
        required=True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES, 'placeholder': _('Enter your password')}), 
        label=_('Password'), 
        required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES, 'placeholder': _('Repeat your password')}), 
        label=_('Repeat password'),
        required=True
    )


class MusicAdviceForm(forms.ModelForm):

    class Meta:
        model = MusicAdvice
        fields = ('base', 'advice', 'description', 'category')
        widgets = {
            'base': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'What you liked'
            }),
            'advice': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'What you advice'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Why do you think it\'s a good advice?'
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                
            })
        }
        labels = {
            'base': _('If you like'),
            'advice': _('You might like'),
            'description': _('Because'),
            'category': _('Category'),
        }

