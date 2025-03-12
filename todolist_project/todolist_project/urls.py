from django.contrib import admin
from django.urls import path, include

from dashboard.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('todolist.urls')),
    path("", DashboardView.as_view(), name="home"),  # Arahkan root ke Dashboard
    path("dashboard/", include("dashboard.urls")),
    path("cth/", include('contoh.urls')),
]
