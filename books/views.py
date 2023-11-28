from django.shortcuts import redirect, render
from rest_framework import generics
from django.contrib.auth import login, logout
from django.contrib import messages
from .serializers import BookSerializer
from .models import Book, Person
from .forms import UserLoginForm, UserRegisterForm
from .tasks import send_test_message


# view авторизации
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'books/login.html', {'form': form})

# view выхода из аккаунта
def user_logout(request):
    logout(request)
    return redirect('home')

# view регистрации
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # в ветке feature/book-management передвинул создание Person до логина, 
            # чтобы исключить ошибку при не успешной регистрации
            Person.objects.create(name=form.cleaned_data['username'], email=form.cleaned_data['email'])
            login(request, user)
            messages.success(request, 'Успешная регистрация')
            send_test_message.delay(form.cleaned_data['email'])
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'books/register.html', {'form': form})

# view главной страницы
def main(request):
    return render(request, 'books/main.html', context={'books': books})

# Вывод всех книг, добавление книги
class BookAPIList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Обновление и удаление книги
class BookAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer