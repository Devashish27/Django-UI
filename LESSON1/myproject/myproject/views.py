# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Hello, world. You're at the myproject HOME page.")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("Hello, world. You're at the myproject ABOUT page.")
    return render(request, 'about.html')
