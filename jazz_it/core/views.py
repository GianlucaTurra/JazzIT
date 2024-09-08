from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Sample view for basic testing
# TODO: implement a proper home
def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/home.html')


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return home(request)
