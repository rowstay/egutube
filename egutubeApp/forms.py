from django import forms
from .models import Post
import os
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# Подключаем модель User
from django.contrib.auth.models import User

class UploadFileForm(forms.Form):
    title = forms.CharField()
    file = forms.FileField()
    body = forms.CharField()

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'cover', 'author', 'body']


# Создаём класс формы
class RegistrForm(UserCreationForm):
  # Добавляем новое поле Email
  email = forms.EmailField(max_length=254, help_text='This field is required')

  # Создаём класс Meta
  class Meta:
    # Свойство модели User
    model = User
    # Свойство назначения полей
    fields = ('username', 'email', 'password1', 'password2', )
