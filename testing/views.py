from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from test_constructor.models import Test, Question, Option


def enter_code(request):
    return render(request, 'testing/codeEntering.html')

def enter_code_again(request):
    return render(request, 'testing/wrongCodeEntering.html')


def open_test(request):
    if request.method == "POST":

        enteredCode = request.POST.get("code")
        if Test.objects.filter(code=enteredCode).count() == 1:

            test = Test()
            test.code = enteredCode
            return HttpResponseRedirect("/testing/run_test/?code={0}".format(test.code))
        else:
            return render(request, 'testing/wrongCodeEntering.html')


def run_test(request):
    code = request.GET.get("code")
    questions = Question.objects.filter(test_code=56317311)
    string = " 123"
    string2 = ""
    for question in questions:
        string111 = question.text

        options = question.option_set.filter(question=question)
        i = 2
        string = ["","","","",""]
        for option in options:
            string[i] = option.text
            i = i + 1

    data = {"question_text": string111, "option1": string[2], "option2": string[3], "option3": string[4]}
    return  render(request, "testing/testRunner.html", context=data)