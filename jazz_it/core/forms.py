from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
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

