from django.shortcuts import render
from .models import Question


def test_constructor(request):
    return render(request, 'test_constructor/testConstructor.html')
