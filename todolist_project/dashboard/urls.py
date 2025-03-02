from django.urls import path
from .views import DashboardView, TaskDataView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('task-data/', TaskDataView.as_view(), name='task_data'),  # API untuk data chart.js
]
