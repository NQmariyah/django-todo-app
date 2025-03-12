from django.contrib import admin
from django.urls import path, include

from contoh.views import contoh

urlpatterns = [
    path('', contoh),
]