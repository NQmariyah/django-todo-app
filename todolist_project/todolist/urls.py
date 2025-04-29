from django.urls import path
from django.contrib.auth import views as auth_views

from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, RegisterView, TaskDetailJsonView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todolist/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<int:pk>/detail/', TaskDetailJsonView.as_view(), name='task_detail_json')
]