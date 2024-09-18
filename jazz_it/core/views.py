from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import MusicAdvice
from .forms import MusicAdviceForm
from .modules.views_utils import Templates, save_new_music_advice, update_music_advice


# Sample view for basic testing
# TODO: implement a proper home
def home(request: HttpRequest) -> HttpResponse:
    music_advices = MusicAdvice.objects.all()
    return render(request, Templates.HOME, {'music_advices': music_advices})


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return home(request)

# TODO: Is `view_util` and the bool return the best way?
@login_required
def add_music_advice(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = MusicAdviceForm()
        return render(request, Templates.ADD_MUSIC_ADVICE, {'form': form, 'submit': 'core:add_music_advice'})
    if request.method == 'POST':
        is_save_successful = save_new_music_advice(request)
        if not is_save_successful:
            return HttpResponse(status=400)
        return HttpResponse(status=200)
    return HttpResponse(status=405)


@login_required
def edit_music_advice(request: HttpRequest, pk: str) -> HttpResponse:
    music_advice = get_object_or_404(MusicAdvice, pk=pk)
    if music_advice.user != request.user:
        return HttpResponse(status=403)
    if request.method == 'GET':
        form = MusicAdviceForm(instance=music_advice)
        return render(request, Templates.ADD_MUSIC_ADVICE, {'form': form, 'submit': 'core:edit_music_advice', 'pk': pk})
    if request.method == 'POST':
        if not update_music_advice(request, music_advice):
            return HttpResponse(400)
        return HttpResponse(status=200)
    return HttpResponse(status=405)


@login_required
def delete_music_advice(request: HttpRequest, pk: str) -> HttpResponse:
    music_advice = get_object_or_404(MusicAdvice, pk=pk)
    if music_advice.user != request.user and not request.user.is_staff: # type: ignore
        return HttpResponse(status=403)
    if request.method != 'DELETE':
        return HttpResponse(status=405)
    music_advice.delete()
    return HttpResponse(status=200)
