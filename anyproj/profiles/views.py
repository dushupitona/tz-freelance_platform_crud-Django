from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from profiles.forms import CustomUserCreationForm, LoginUserForm, CustomerForm, ExecutorForm
from profiles.models import CustomerModel, ExecutorModel


class RegView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'profiles/reg.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
        login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    form_class =  LoginUserForm
    template_name = 'profiles/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_view(request):
    logout(request)
    return redirect('/')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/profile.html' 
    login_url = reverse_lazy('login')

    customer = CustomerModel
    executor = ExecutorModel
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['slug'] = slug
        if slug == self.customer.slug():
            profile, created = self.customer.objects.get_or_create(user=self.request.user)
            context['bar_title'] = 'Customer'
            context['profile'] = profile
            context['form_class'] = CustomerForm
            context['form'] = CustomerForm(initial={'phone': profile.phone})
        elif slug == self.executor.slug():
            profile, created = self.executor.objects.get_or_create(user=self.request.user)
            context['bar_title'] = 'Executor'
            context['profile'] = profile
            context['form_class'] = ExecutorForm
            context['form'] = ExecutorForm(initial={'phone': profile.phone, 'experience': profile.experience or 'ASD', 'exp_description': profile.exp_description})
        return context  
    
    def post(self, request, **kwargs):
        form_class = self.get_context_data()['form_class']
        form = form_class(request.POST)
        if form.is_valid():
            try:
                model = form_class.model().objects.get(user=self.request.user)
                if model.__class__ is self.customer:
                    model.phone = form.cleaned_data.get('phone')
                    model.save()
                elif model.__class__ is self.executor:
                    model.phone = form.cleaned_data.get('phone')
                    model.experience = form.cleaned_data.get('experience')
                    model.exp_description = form.cleaned_data.get('exp_description')
                    model.save()
                else:
                    raise HttpResponseNotFound
                
            except:
                return HttpResponseNotFound()
        else:
            return self.render_to_response(self.get_context_data(form=form, errors='Invalid input!'))
        return self.render_to_response(self.get_context_data())
    

class IndexView(TemplateView):
    template_name = 'profiles/index.html'


class ChoiseView(TemplateView):
    template_name = 'profiles/profile_type.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = CustomerModel.slug()
        context['executor'] = ExecutorModel.slug()
        return context
