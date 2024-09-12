from django.contrib.auth.forms import AuthenticationForm
from django import forms


INPUT_CLASSES = 'border border-extra text-secondary rounded-lg block w-full'


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
