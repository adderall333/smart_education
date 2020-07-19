from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Test, Question, Option
import datetime


def index(request):
    return render(request, 'test_constructor/index.html')


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
    questions = Question.objects.filter(test_title=test)
    return render(request, "test_constructor/testConstructor.html",
                  {"questions": questions, "test": test})


def add_question(request):
    if request.method == "POST":
        question = Question()
        test = request.GET.get("test")
        question.test_title = test
        question.id = request.GET.get("id")
        question.text = request.POST.get("text")
        question.image = request.POST.get("image")
        question.save()
        for i in range(20):
            try:
                option = Option()
                option.text = request.POST.get("option" + str(i + 1))
                option.question = question
                option.is_correct = request.POST.get("correct" + str(i + 1)) == "on"
                option.save()
            except:
                break
        return HttpResponseRedirect("/test_constructor/new_test/?test={0}".format(test))


def edit(request):
    try:
        id = request.GET.get("id")
        question = Question.objects.get(id=id)
        options = question.option_set.all()

        if request.method == "POST":
            test = request.GET.get("test")
            question.text = request.POST.get("text")
            question.image = request.POST.get("image")
            question.save()
            i = 0
            for option in options:
                try:
                    option.text = request.POST.get("option" + str(i + 1))
                    option.is_correct = request.POST.get("correct" + str(i + 1)) == "on"
                    option.save()
                    i += 1
                except:
                    break
            for j in range(i, 20 - options.count()):
                try:
                    option = Option()
                    option.text = request.POST.get("option" + str(j + 1))
                    option.question = question
                    option.is_correct = request.POST.get("correct" + str(j + 1)) == "on"
                    option.save()
                except:
                    break
            return HttpResponseRedirect("/test_constructor/new_test/?test={0}".format(test))
        else:
            return render(request, "test_constructor/edit.html", {"question": question, "options": options})
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")


def delete(request):
    try:
        id = request.GET.get("id")
        test = request.GET.get("test")
        question = Question.objects.get(id=id)
        question.delete()
        return HttpResponseRedirect("/test_constructor/new_test/?test={0}".format(test))
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")
