from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from test_constructor.models import Test, Question, Option


def enter_code(request):
    return render(request, 'testing/codeEntering.html')


def open_test(request):
    if request.method == "POST":

        entered_code = request.POST.get("code")
        if Test.objects.filter(code=entered_code).count() == 1:

            test = Test()
            test.code = entered_code
            return HttpResponseRedirect("/testing/run_test/?code={0}".format(test.code))
        else:
            return render(request, 'testing/wrongCodeEntering.html')


def run_test(request):
    code = request.GET.get("code")
    questions = {}
    i = 0
    for question in Question.objects.filter(test_code=code):
        options = question.option_set.filter(question=question)
        true_answers = 0
        for option in question.option_set.all():
            if option.is_correct:
                true_answers += 1

        if options.count() == 0:
            type = 1
        elif true_answers == 1:
            type = 2
        else:
            type = 3
        d = {"text": question.text,
             "image": question.image,
             "amount_of_points": question.amount_of_points,
             "options": options,
             "question_type": type}
        questions[i] = d
        i += 1
    data = {"questions": questions}

    return  render(request, "testing/testRunner.html", context=data)


#{{ value|linebreaksbr }}




# string = " 123"
# string2 = ""
# for question in questions:
#     string111 = question.text
#
#     options = question.option_set.filter(question=question)
#     i = 2
#     string = ["","","","",""]
#     for option in options:
#         string[i] = option.text
#         i = i + 1















