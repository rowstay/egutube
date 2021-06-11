from django.shortcuts import render, get_object_or_404
from .forms import UploadFileForm
from django import forms
from .models import Post
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrForm
from django.contrib.auth.decorators import login_required
def home(request):

    return render(request,
    'indexApp/homePage.html'
    )

class PageView(ListView):

    model = Post
    template_name = 'indexApp/video.html'

class CreatePost(CreateView): # новый
    model = Post
    form_class = PostForm
    template_name = 'indexApp/post.html'
    success_url = reverse_lazy('home')


def regpage(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = RegistrForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'indexApp/homePage.html', data)
    else:
        # Создаём форму
        form = RegistrForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'indexApp/regpage.html', data)
