from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from django.views.generic import CreateView, FormView
from django.views.generic.base import View

from account.forms import RegistrationForm, LoginForm
from account.models import Account
from account.tasks import send_password


class RegistrationView(CreateView):
    model = Account
    form_class = RegistrationForm
    success_url = '/login'
    template_name = 'account/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        send_password.delay(user.id)
        return super().form_valid(form)


class AuthenticationForm(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form, ):
        if form.is_valid():
            email = self.request.POST['email']
            password = self.request.POST['password']
            user = authenticate(email=email, password=password)
            login(self.request, user)
            return redirect('home')
        else:
            form = LoginForm()
        return render(self.request, 'account/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('account:login')

