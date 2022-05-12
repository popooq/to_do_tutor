from multiprocessing import context
from django.shortcuts import render, redirect
from pkg_resources import require
from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', 
    {'title': 'Главная страница сайта', 'tasks' : tasks})


def about_us(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form' : form,
        'error' : error
    }
    return render(request, 'main/create.html', context)