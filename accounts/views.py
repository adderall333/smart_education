from django.contrib.auth import authenticate, login
from .models import MyUserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from test_constructor.models import Test, Question
from testing.models import TestResult, QuestionResult, OptionResult


def all_results(request):
    code = request.GET.get("code")

    if Test.objects.get(code=code).author != request.user:
        return HttpResponse("<h2>У вас нет доступа к этому тесту</h2>")

    test_results = TestResult.objects.filter(test=Test.objects.get(code=code))
    return render(request, 'accounts/all_results.html', {"test_results": test_results})


def results(request):
    code = request.GET.get("code")

    if Test.objects.get(code=code).author != request.user:
        return HttpResponse("<h2>У вас нет доступа к этому тесту</h2>")

    test = Test.objects.get(code=code)
    user = request.GET.get("user")
    test_result = TestResult.objects.filter(test=test).get(user=user)
    questions = {}
    i = 0
    for question in Question.objects.filter(test_code=code):
        d = {"text": question.text,
             "image": question.image,
             "amount_of_points": question.amount_of_points,
             "options": question.option_set.all()}
        questions[i] = d
        i += 1
    data = {"test_result": test_result, "test": test, "questions": questions}
    return render(request, "accounts/results.html", context=data)


class SignUpView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def signup(self):
        if self.method == 'POST':
            form = MyUserCreationForm(self.POST)
            if form.is_valid():
                form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(self, user)
            return redirect('index')
        else:
            form = MyUserCreationForm()
        return render(self, 'accounts/signup.html', {'form': form})


class Account:

    def home(self):
        tests = Test.objects.filter(author=self.user)
        return render(self, 'accounts/home.html', {"tests": tests})
