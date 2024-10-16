from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

from .models import MusicAdvice, UserProfile
from .forms import MusicAdviceForm, SignUpForm
from .modules.views_utils import Templates, save_new_music_advice, update_music_advice, create_new_user, get_user


# Sample view for basic testing
# TODO: implement a proper home
# TODO: clearly needs refactoring
def home(request: HttpRequest) -> HttpResponse:
    music_advices = MusicAdvice.objects.all()
    data: dict[str, object] = {'music_advices': music_advices}
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(pk=request.user)
        data['profile'] = user_profile
        data['music_advices'] = music_advices.exclude(user=request.user)
    return render(request, Templates.HOME, data)


def signup(request: HttpRequest) -> HttpResponse:
    match request.method:
        case 'GET':
            form = SignUpForm()
            return render(request, Templates.SIGNUP, {'form': form})
        case 'POST':
            form = SignUpForm(request.POST)
            if not create_new_user(form):
                return render(request, Templates.SIGNUP, {'form': form})
            user = get_user(request)
            if user is not None:
                login(request, user)
            else:
                return render(request, Templates.SIGNUP, {'form': form})
            return redirect('/')
    return HttpResponse(status=405)


def profile(request: HttpRequest) -> HttpResponse:
    ...


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return home(request)


# TODO: Is `view_util` and the bool return the best way?
@login_required
def add_music_advice(request: HttpRequest) -> HttpResponse:
    match request.method:
        case 'GET':
            form = MusicAdviceForm()
            return render(request, Templates.ADD_MUSIC_ADVICE, {'form': form, 'submit': 'core:add_music_advice'})
        case 'POST':
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
    match request.method:
        case 'GET':
            form = MusicAdviceForm(instance=music_advice)
            return render(request, Templates.ADD_MUSIC_ADVICE, {'form': form, 'submit': 'core:edit_music_advice', 'pk': pk})
        case 'POST':
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
