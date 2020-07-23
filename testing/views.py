from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf

from test_constructor.models import Test, Question, Option

from testing.models import TestResult, QuestionResult, OptionResult


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
             "question_type": type,
             "id": question.id}
        questions[i] = d
        i += 1
    data = {"questions": questions, "code": code, "questions_number": len(questions), "first_question_id": questions[0]["id"]}

    return  render(request, "testing/testRunner.html", context=data)

def send_answers(request, code, questions_number):
    if request.method == 'POST':

        test_result = TestResult()
        test_result.test = Test.objects.get(code=code)
        test_result.user = request.POST.get("user_name")
        test_result.save()

        question_results = []

        test_result.amount_of_points = 0

        question_list = list(Question.objects.filter(test_code=code).values())

        for i in range (int(questions_number)):
            question_results.append(2)
            question_results[i] = QuestionResult()

            question_results[i].test_result = test_result
            question_results[i].question = Question.objects.get(id=question_list[i]["id"])

            question_results[i].test_answer = request.POST.get("answer_" + str(question_list[i]["id"]))
            #       если будет ругаться то добавить иф на тип вопроса перед строчкой выше

            question_results[i].amount_of_points = question_results[i].question.amount_of_points


            option_list = list(question_results[i].question.option_set.values())

            option_results = []

            for j in range (len(option_list)):
                option_results.append(2)
                option_results[j] = OptionResult()
                option_results[j].question_result = question_results[i]
                option_results[j].is_selected = request.POST.get("q_" + str(question_list[i]["id"]))

                if (option_results[j].is_selected != option_list[j]["is_correct"]) or (not option_results[j].is_selected == option_list[j]["is_correct"]):
                    question_results[i].amount_of_points = 0
            test_result.amount_of_points += question_results[i].amount_of_points

    return HttpResponse("<h2> Вы прошли тест, резы у препода, на главную сами перейдёте </h2> ")



# entry_list = list(Entry.objects.all())


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















