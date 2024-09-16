from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_ma/', views.add_music_advice, name='add_music_advice'),
]