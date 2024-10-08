from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_email(email: str):
    if User.objects.filter(email__iexact=email).exists():
        raise ValidationError('This email address is already in use.')
