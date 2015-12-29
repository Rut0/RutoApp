from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'title': 'Home Page'}
    return render(request, 'base.html', context)
