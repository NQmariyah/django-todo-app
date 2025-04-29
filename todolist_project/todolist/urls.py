from django.urls import path
from django.contrib.auth import views as auth_views

from . import views_drf
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, RegisterView, TaskDetailJsonView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todolist/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<int:pk>/detail/', TaskDetailJsonView.as_view(), name='task_detail_json'),










    path('api/tasks/', views_drf.TaskListCreateView.as_view(), name='task-list-create'),
    path('api/my-tasks/', views_drf.MyTaskListView.as_view(), name='my-task-list'),
    path('api/tasks/<int:pk>/', views_drf.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),

    # Task detail simple
    path('api/tasks/<int:pk>/json/', views_drf.TaskDetailJsonView.as_view(), name='task-detail-json'),

    # User register API
    path('api/register/', views_drf.RegisterView.as_view(), name='register'),
]