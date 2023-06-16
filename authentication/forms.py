from django import forms
from .models import *
from django.contrib.auth.models import User


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your Email address'
        self.fields['password'].widget.attrs['placeholder'] = 'Create your password'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"


    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
        'password': forms.PasswordInput()
        }
