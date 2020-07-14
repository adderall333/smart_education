from django.shortcuts import render
from .models import Question


def test_constructor(request):
    questions = Question.objects.all()
    return render(request, 'test_constructor/testConstructor.html', {"questions": questions})
