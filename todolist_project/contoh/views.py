from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def contoh(request):
    return HttpResponse("Selamat Datang")
