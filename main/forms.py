from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


class CreateAndReadCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'deadline', 'priority']


class CreateSubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['content']


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'deadline', 'priority', 'active']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-input'})
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )