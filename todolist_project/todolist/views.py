from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '')

        if search_query:
            context['other_tasks'] = Task.objects.filter(
                Q(title__icontains=search_query) & ~Q(user=self.request.user)
            )
        else:
            context['other_tasks'] = Task.objects.exclude(user=self.request.user)

        context['my_tasks'] = Task.objects.filter(user=self.request.user)
        return context


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
    template_name = 'task_confirm_delete.html'  # Optional, jika menggunakan template konfirmasi
    success_url = reverse_lazy('task_list')  # Redirect setelah berhasil dihapus

    def delete(self, request, *args, **kwargs):
        # Override untuk menangani permintaan AJAX dengan JsonResponse
        if request.is_ajax():
            task = self.get_object()
            task.delete()
            return JsonResponse({'message': 'Tugas berhasil dihapus'}, status=200)
        return super().delete(request, *args, **kwargs)


class TaskDetailJsonView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        data = {
            'title': task.title,
            'completed': task.completed,
            'creator': task.user.username,
        }
        return JsonResponse(data)


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'todolist/register.html'
    success_url = reverse_lazy('login')