from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    created_on = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks, 'created_on': created_on})


def about(request):
    return render(request, 'main/about_us.html')


def my_page(request):
    return render(request, 'main/my_page.html')
