from django.contrib.auth import authenticate, login
from .models import MyUserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from test_constructor.models import Test


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

    def test(self, test_id):
        try:
            test = Test.objects.get(id=test_id)
        except:
            raise Http404("Тест не найден")

        return render(self, 'accounts/test.html', {'accounts': test})
