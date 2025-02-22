from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'todolist/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todolist/task_create.html'
    success_url = reverse_lazy('task_list')


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'todolist/task_update.html', {'form': form, 'task': task})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'todolist/task_delete.html', {'task': task})