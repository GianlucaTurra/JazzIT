from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Suggestion


# Sample view for basic testing
# TODO: implement a proper home
def home(request: HttpRequest) -> HttpResponse:
    suggestions = Suggestion.objects.all()
    return render(request, 'core/home.html', {'suggestions': suggestions})


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return home(request)
