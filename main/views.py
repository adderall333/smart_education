from django.shortcuts import render
import random


def menu(request):
    return render(request, 'main/menu.html')