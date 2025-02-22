from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todolist/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Arahkan kembali ke daftar tugas setelah sukses
    else:
        form = TaskForm()

    return render(request, 'todolist/task_create.html', {'form': form})
