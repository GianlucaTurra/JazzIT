from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import MusicAdvice
from .validators import validate_email

INPUT_CLASSES = 'border border-extra rounded-lg block w-full text-inputs'


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': _('Username')}),
        label=_('Username'),
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES, 'placeholder': _('Password')}),
        label=_('Password'),
        required=True,
    )


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
        required=True,
        validators=[validate_email]
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

