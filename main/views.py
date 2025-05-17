from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Привет! Это мой одностраничник на Django</h1>")
# Create your views here.
