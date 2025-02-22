from django.urls import path
from .views import task_create, task_update, task_delete, TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:task_id>/', task_update, name='task_update'),
    path('delete/<int:task_id>/', task_delete, name='task_delete'),
]