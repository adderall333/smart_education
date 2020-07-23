from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.core.exceptions import PermissionDenied
from .models import Test, Question, Option
from testing.models import TestResult

import datetime
import random


def index(request):
    return render(request, 'test_constructor/index.html')


def save_as_new(request):
    code = request.GET.get("code")
    return render(request, "test_constructor/saveAsNew.html", {"code": code})


def add_test(request):
    if request.method == "POST":
        test = Test()
        test.title = request.POST.get("title")
        test.author = request.user
        test.pub_date = datetime.datetime.now()
        while True:
            code = random.randint(10000000, 99999999)
            if Test.objects.filter(code=code).count() == 0:
                test.code = code
                break
        test.save()
        return HttpResponseRedirect("/test_constructor/test/?code={0}".format(test.code))


def save_test(request):
    if request.method == "POST":
        test = Test()
        test.title = request.POST.get("title")
        test.author = request.user
        test.pub_date = datetime.datetime.now()
        while True:
            code = random.randint(10000000, 99999999)
            if Test.objects.filter(code=code).count() == 0:
                test.code = code
                break
        test.save()
        previous_code = request.GET.get("code")
        previous_questions = Question.objects.filter(test_code=previous_code)
        for previous_question in previous_questions:
            question = Question()
            question.test_code = test.code
            question.text = previous_question.text
            question.image = previous_question.image
            question.amount_of_points = previous_question.amount_of_points
            question.save()
            previous_options = previous_question.option_set.all()
            for previous_option in previous_options:
                option = Option()
                option.question = question
                option.text = previous_option.text
                option.is_correct = previous_option.is_correct
                option.save()
        return HttpResponseRedirect("/test_constructor/test/?code={0}".format(test.code))


def new_test(request):
    code = request.GET.get("code")

    if Test.objects.get(code=code).author != request.user:
        raise PermissionDenied

    if Test.objects.get(code=code).testresult_set.all().count() == 0:
        questions = Question.objects.filter(test_code=code)
        return render(request, "test_constructor/testConstructor.html",
                      {"questions": questions, "code": code, "already_used": False})
    else:
        return render(request, "test_constructor/testConstructor.html", {"code": code, "already_used": True})


def add_question(request):
    if request.method == "POST":
        question = Question()
        code = request.GET.get("code")

        if Test.objects.get(code=code).author != request.user:
            raise PermissionDenied

        question.test_code = code
        question.id = request.GET.get("id")
        question.text = request.POST.get("text")
        question.amount_of_points = request.POST.get("amount_of_points")
        question.image = request.FILES.get("image")
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
        return HttpResponseRedirect("/test_constructor/test/?code={0}".format(code))


def edit(request):
    try:
        code = request.GET.get("code")

        if Test.objects.get(code=code).author != request.user:
            raise PermissionDenied

        id = request.GET.get("id")
        question = Question.objects.get(id=id)
        options = question.option_set.all()

        if request.method == "POST":
            question.text = request.POST.get("text")
            question.amount_of_points = request.POST.get("amount_of_points")
            if request.FILES.get("image"):
                question.image = request.FILES.get("image")
            question.save()
            for option in options:
                try:
                    option.delete()
                except:
                    break
            for i in range(20):
                try:
                    option = Option()
                    option.text = request.POST.get("option" + str(i + 1))
                    option.question = question
                    option.is_correct = request.POST.get("correct" + str(i + 1)) == "on"
                    option.save()
                except:
                    break
            return HttpResponseRedirect("/test_constructor/test/?code={0}".format(code))
        else:
            return render(request, "test_constructor/edit.html", {"question": question, "options": options})
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")


def delete(request):
    try:
        id = request.GET.get("id")
        code = request.GET.get("code")

        if Test.objects.get(code=code).author != request.user:
            raise PermissionDenied

        question = Question.objects.get(id=id)
        question.delete()
        return HttpResponseRedirect("/test_constructor/test/?code={0}".format(code))
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")


def delete_test(request):
    try:
        code = request.GET.get("code")

        if Test.objects.get(code=code).author != request.user:
            raise PermissionDenied

        test = Test.objects.get(code=code)
        questions = Question.objects.filter(test_code=code)
        for question in questions:
            question.delete()
        test.delete()
        return HttpResponseRedirect("/accounts/home/")
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")
    except Test.DoesNotExist:
        return HttpResponseNotFound("<h2>Test not found</h2>")
