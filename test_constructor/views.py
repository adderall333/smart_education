from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Test, Question, TestForm, QuestionForm
import datetime


def index(request):
    return render(request, 'test_constructor/index.html', {"form": TestForm})


def add_test(request):
    if request.method == "POST":
        test = Test()
        test.title = request.POST.get("title")
        test.author = request.user
        test.pub_date = datetime.datetime.now()
        test.save()
        return HttpResponseRedirect("/test_constructor/new_test/?test={0}".format(test.title))


def new_test(request):
    test = request.GET.get("test")
    url = "/test_constructor/add_question/?test={0}".format(test)
    questions = Question.objects.filter(test_title=test)
    return render(request, "test_constructor/testConstructor.html", {"questions": questions, "form": QuestionForm, "url": url})


def add_question(request):
    if request.method == "POST":
        question = Question()
        test = request.GET.get("test")
        question.test_title = test
        question.options_count = request.POST.get("options_count")
        question.text = request.POST.get("text")
        question.image = request.POST.get("image")
        question.options = request.POST.get("options")
        question.correct_answer = request.POST.get("correct_answer")
        question.save()
        return HttpResponseRedirect("/test_constructor/new_test/?test={0}".format(test))


def edit(request):
    try:
        text = request.GET.get("text")
        question = Question.objects.get(text=text)

        if request.method == "POST":
            test = request.GET.get("test")
            question.options_count = request.POST.get("options_count")
            question.text = request.POST.get("text")
            question.image = request.POST.get("image")
            question.options = request.POST.get("options")
            question.correct_answer = request.POST.get("correct_answer")
            question.save()
            return HttpResponseRedirect("/test_constructor/new_test/?test={0}".format(test))
        else:
            return render(request, "test_constructor/edit.html", {"question": question})
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")
