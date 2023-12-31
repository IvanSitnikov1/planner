from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


class CreateAndReadCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'id': "enter-content",
                'placeholder': "Напишите комментарий"
            }),
        }


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'deadline', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'id': "enter-header", 'placeholder':"Введите название задачи"}),
            'content': forms.Textarea(attrs={'id': "enter-content", 'placeholder':"Опишите задачу"}),
            'deadline': forms.TextInput(attrs={'id': "enter-deadline", 'type': 'date'}),
            'priority': forms.Select(attrs={'id': "enter-priority"})
        }


class CreateSubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'id': "enter-content",
                'placeholder': "Опишите подзадачу"
            }),
        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'deadline', 'priority', 'active']
        widgets = {
            'title': forms.TextInput(attrs={'id': "enter-header",
                                            'placeholder': "Введите название задачи"}),
            'content': forms.Textarea(attrs={'id': "enter-content",
                                             'placeholder': "Опишите задачу"}),
            'deadline': forms.TextInput(
                attrs={'id': "enter-deadline", 'type': 'date'}),
            'priority': forms.Select(attrs={'id': "enter-priority"})
        }


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
