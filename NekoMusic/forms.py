from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

class Registro(UserCreationForm):
    pass
class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput)