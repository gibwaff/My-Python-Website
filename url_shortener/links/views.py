from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import ShortenedLink
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm, UserProfileForm
import random
import string

def home(request):
    return render(request, 'links/home.html')

def about(request):
    return render(request, 'links/about.html')

def redirect_link(request, name):
    try:
        link = ShortenedLink.objects.get(name=name)
        return HttpResponseRedirect(link.address)
    except ShortenedLink.DoesNotExist:
        return render(request, '404.html', status=404)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Установка пароля
            user.save()
            login(request, user)  # Вход пользователя после регистрации
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'links/register.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    if request.method == 'POST':
        # Обновление логина
        username = request.POST.get('username', '').strip()
        if username:
            user.username = username
        
        # Обновление email
        email = request.POST.get('email', '').strip()
        if email:
            user.email = email
        
        user.save()  # Сохраняем изменения
        return redirect('dashboard')  # Перенаправление на личный кабинет после сохранения

    return render(request, 'links/dashboard.html', {'user': user})

@login_required
def shorten_link(request):
    user_links = ShortenedLink.objects.filter(user=request.user)  # Получение всех сокращенных ссылок пользователя

    if request.method == 'POST':
        original_url = request.POST['original_url']
        custom_shortened_url = request.POST.get('custom_shortened_url', '').strip()

        # Проверка на уникальность пользовательского значения
        if custom_shortened_url:
            # Проверяем, существует ли уже сокращенная ссылка с таким же значением для данного пользователя
            if ShortenedLink.objects.filter(user=request.user, name=custom_shortened_url).exists():
                return render(request, 'links/shorten_link.html', {
                    'error': 'Это сокращенное значение уже занято для вас. Пожалуйста, выберите другое.',
                    'user_links': user_links
                })

        # Генерация случайного сокращенного значения, если пользователь не ввел свое
        if not custom_shortened_url:
            custom_shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        # Создание новой сокращенной ссылки
        ShortenedLink.objects.create(user=request.user, name=custom_shortened_url, address=original_url)
        return redirect('shorten_link')

    return render(request, 'links/shorten_link.html', {'user_links': user_links})
