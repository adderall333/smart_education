from django.contrib.auth import authenticate, login
from .models import MyUserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from test_constructor.models import Test
from testing.models import TestResult, QuestionResult, OptionResult


def results(request):
    code = request.GET.get("code")
    test_result = TestResult.objects.get(test_code=code)
    questions_results = QuestionResult.object.filter(test_result=test_result)
    return render('accounts/results.html', {"test": test_result, "questions": questions_results})


class SignUpView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def signup(self):
        if self.method == 'POST':
            form = MyUserCreationForm(self.POST)
            if form.is_valid():
                form.save()
            username = form.cleaned_data.get('email')
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
