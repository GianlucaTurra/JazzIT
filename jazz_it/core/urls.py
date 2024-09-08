from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import LoginForm
import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_user, name='logout'),
]