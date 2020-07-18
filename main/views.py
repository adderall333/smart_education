from django.shortcuts import render


def menu(request):
    return render(request, 'main/menu.html')


def signin(request):
    return render(request, 'main/signin.html')


def signup(request):
    return render(request, 'main/signup.html')
