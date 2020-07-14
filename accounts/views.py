from django.contrib.auth import authenticate, login
from .models import MyUserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

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
            return render(self, 'templates.signup.html', {'form': form})



