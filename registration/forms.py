from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")
    fields = ("username", "email", "password1", "password2")
