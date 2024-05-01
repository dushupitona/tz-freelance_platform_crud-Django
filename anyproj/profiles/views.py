from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from profiles.forms import LoginForm, RegForm
# Create your views here.


class RegView(FormView):
    template_name = 'profiles/reg.html'
    form_class = RegForm

class LoginView(FormView):
    template_name = 'profiles/login.html'
    form_class = LoginForm


class ProfileView(TemplateView):
    template_name = 'profiles/index.html'