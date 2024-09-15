from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import MusicAdvise
from .modules.views_utils import Templates


# Sample view for basic testing
# TODO: implement a proper home
def home(request: HttpRequest) -> HttpResponse:
    music_advices = MusicAdvise.objects.all()
    return render(request, Templates.HOME, {'music_advices': music_advices})


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return home(request)


@login_required
def add_music_advice(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, Templates.ADD_MUSIC_ADVICE)
    if request.method == 'POST':
        # TODO handle request properly with a function
        return render(request, Templates.ADD_MUSIC_ADVICE)
    return HttpResponse(status=405)


@login_required
def edit_music_advice(request: HttpRequest, pk: str) -> HttpResponse:
    music_advice = get_object_or_404(MusicAdvise, pk)
    if music_advice.user != request.user:
        return HttpResponse(status=403)
    if request.method == 'GET':
        return render(request, Templates.EDIT_MUSIC_ADVICE)
    if request.method == 'POST':
        # TODO handle request properly with a function
        pass
    return HttpResponse(status=405)


@login_required
def delete_music_advice(request: HttpRequest, pk: str) -> HttpResponse:
    music_advice = get_object_or_404(MusicAdvise, pk)
    if music_advice.user != request.user and not request.user.is_staff: # type: ignore
        return HttpResponse(status=403)
    if request.method != 'DELETE':
        return HttpResponse(status=405)
    music_advice.delete()
    return HttpResponse(status=200)
