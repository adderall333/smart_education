from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Test, Question, TestForm, QuestionForm


def index(request):
    return render(request, 'test_constructor/index.html', {"form": TestForm})


def add_test(request):
    if request.method == "POST":
        test = Test()
        test.title = request.POST.get("title")
        test.save()
    return HttpResponseRedirect("/test_constructor")


def test_constructor(request):
    questions = Question.objects.all()
    return render(request, "testConstructor.html", {"questions": questions, "form": QuestionForm})


def add_question(request):
    if request.method == "POST":
        question = Question()
        question.test = request.POST.get("test")
        question.with_options = request.POST.get("with_options")
        question.text = request.POST.get("text")
        question.image = request.POST.get("image")
        question.options = request.POST.get("options")
        question.correct_answer = request.POST.get("correct_answer")
        question.save()
    return HttpResponseRedirect("/test_constructor")