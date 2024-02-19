from django.shortcuts import render
from django.http import HttpResponse


def news_list(request):
    return HttpResponse('<h1>Новости</h1>')
# Create your views here.
