from django.views.generic import TemplateView, View
from django.http import JsonResponse
from todolist.models import Task
from django.db.models import Count


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'


class TaskDataView(View):
    def get(self, request, *args, **kwargs):
        completed_tasks = Task.objects.filter(completed=True).count()
        pending_tasks = Task.objects.filter(completed=False).count()

        tasks_per_user = Task.objects.values('user__username').annotate(task_count=Count('id'))

        return JsonResponse({
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'tasks_per_user': list(tasks_per_user),
        })
