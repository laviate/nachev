from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Rango says hey there partner!")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("Rango says hey there partner!")
    return render(request, 'about.html')


def why_plastic(request):
    # return HttpResponse("Rango says hey there partner!")
    return render(request, 'why_plastic.html')


def products(request):
    # return HttpResponse("Rango says hey there partner!")
    return render(request, 'products.html')


def news(request):
    # return HttpResponse("Rango says hey there partner!")
    return render(request, 'news.html')
