from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from phonenumber_field.formfields import PhoneNumberField
from profiles.models import CustomerModel, ExecutorModel


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'id': 'custom-username', 'class': 'my-class'}),
            'email': forms.EmailInput(attrs={'id': 'custom-email', 'class': 'my-class'}),
            'first_name': forms.TextInput(attrs={'id': 'custom-first-name', 'class': 'my-class'}),
            'last_name': forms.TextInput(attrs={'id': 'custom-last-name', 'class': 'my-class'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
 
    class Meta:
        model = User
        fields = ('username', 'password')


class CustomerForm(forms.Form):
    phone = PhoneNumberField()

    @classmethod
    def model(cls):
        return CustomerModel
        

class ExecutorForm(forms.Form):
    phone = PhoneNumberField()
    experience = forms.IntegerField(min_value=1, max_value=100)
    exp_description = forms.CharField(widget=forms.Textarea)
    
    @classmethod
    def model(cls):
        return ExecutorModel