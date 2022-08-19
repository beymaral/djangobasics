from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    hello = '<h1>Hello World</h1>'
    return HttpResponse(hello)
