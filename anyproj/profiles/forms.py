from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import MultiWidget


class RegForm(UserCreationForm):
    name = forms.CharField(max_length=32, label='Name')
    surname = forms.CharField(max_length=32, label='Surname')
    phone  = PhoneNumberField(region='RU')

    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'email', 'phone', 'password1', 'password2')
        widgets = {
        'username': forms.TextInput(attrs={
            'name': 'username',
            'id': 'id_form_username'
        }),

        'name': forms.TextInput(attrs={
            'name': 'name',
            'id': 'id_form_name'
        }),

        'surname': forms.TextInput(attrs={
            'name': 'surname',
            'id': 'id_form_name'
        }),

        'email': forms.EmailInput(attrs={
            'name': 'surname',
            'id': 'id_form_email' 
        }),

        'phone': forms.TextInput(attrs={
            'name': 'phone',
            'id': 'id_form_phone'
        }),

        'password1': forms.PasswordInput(attrs={
            'name': 'passwrod1',
            'id': 'id_form_password1'
        }),
        'password2': forms.PasswordInput(attrs={
            'name': 'password2',
            'id': 'id_form_password2'
        })
    }



class LoginForm(AuthenticationForm):
    username  = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
            'name': 'username',
            'id': 'id_form_username'
        }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
            'name': 'password2',
            'id': 'id_form_password2'
        }))


