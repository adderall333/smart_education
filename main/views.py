from django.shortcuts import render

# В зависимости от какого url адреса мы будем показывать какой html шаблон

# Create your views here.

def menu(request):
    return render(request, 'main/menu.html')


def signin(request):
    return render(request, 'main/signin.html')


def signup(request):
    return render(request, 'main/signup.html')
