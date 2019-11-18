from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'authservice/index.html', context=None)


def signin(request):
    return render(request, 'authservice/index.html', context=None)


def signup(request):
    return render(request, 'authservice/index.html', context=None)


def forgot_password(request):
    return render(request, 'authservice/forgot_password.html', context=None)
