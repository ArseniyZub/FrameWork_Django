from django.shortcuts import render

def home(request):
    context = {
        'title': 'Добро пожаловать на мой первый Django-сайт!',
        'content': 'Это мой первый опыт создания веб-приложения с использованием Django.'
    }
    return render(request, 'myapp/home.html', context)

def about(request):
    context = {
        'title': 'Обо мне',
        'content': 'Привет! Я разработчик на python. '
                   'Этот сайт создан для практики работы с Django.'
    }
    return render(request, 'myapp/about.html', context)


