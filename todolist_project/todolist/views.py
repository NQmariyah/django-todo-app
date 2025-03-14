from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm

#ini file views
class TaskListView(ListView):
    model = Task
    template_name = 'todolist/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todolist/task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todolist/task_update.html'
    success_url = reverse_lazy('task_list')

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todolist/task_delete.html'
    success_url = reverse_lazy('task_list')

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'todolist/register.html'
    success_url = reverse_lazy('login')