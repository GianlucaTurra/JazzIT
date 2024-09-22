from django.http import HttpRequest
from django.forms import ModelForm

from ..models import MusicAdvice
from ..forms import MusicAdviceForm, SignUpForm


class Templates:
    """
    Enumeration containing the html templates qualified names to use as 
    constants inside the views.py module
    """
    HOME = 'core/home.html'
    ADD_MUSIC_ADVICE = 'core/add_music_advice.html'
    EDIT_MUSIC_ADVICE = 'core/edit_music_advice.html'
    SIGNUP = 'core/signup.html'


def create_new_user(request: HttpRequest) -> bool:
    form = SignUpForm(request.POST)
    if not form.is_valid():
        return False
    form.save()
    return True


# TODO: il nome e la gestione sono da rivedere
def save_new_music_advice(request: HttpRequest) -> bool:
    form: ModelForm = MusicAdviceForm(request.POST)
    if not form.is_valid():
        return False
    music_advice: MusicAdvice = form.save(commit=False)
    music_advice.user = request.user # type: ignore
    music_advice.save()
    return True


def update_music_advice(request: HttpRequest, music_advice: MusicAdvice) -> bool:
    form: ModelForm = MusicAdviceForm(request.POST, instance=music_advice)
    if not form.is_valid():
        return False
    form.save()
    return True
