from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from phonenumber_field.formfields import PhoneNumberField



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


class ProfileTypeForm(forms.Form):
    profile_type = forms.ChoiceField(choices=[('Customer', 'customer'),('Executor', 'executor')], label='Who are u ?')