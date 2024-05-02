from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.forms import CustomUserCreationForm, ProfileTypeForm
# Create your views here.


class ExecutorRegView(FormView):    
    form_class = CustomUserCreationForm
    template_name = 'profiles/reg.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
        login(self.request, user)
        return super().form_valid(form)
    

class Test(TemplateView):
    user_form = CustomUserCreationForm
    profile_type_form = ProfileTypeForm
    template_name  = 'profiles/reg.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.user_form()
        context['type_form'] = self.profile_type_form
        return context
        


# class CustomerRegView(View):
#     def get_context_data(self, request, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["user_form"] = CustomUserCreationForm()
#         context["executor_form"] = CustomerRegForm
#         return context
    


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/profile.html'
    login_url = reverse_lazy('registration')    


class IndexView(TemplateView):
    template_name = 'profiles/index.html'


class ChoiseView(TemplateView):
    template_name = 'profiles/choise.html'






# user = User.objects.create_user(username='john', password='doe')
# profile = Profile.objects.create(user=user, bio='A short bio')