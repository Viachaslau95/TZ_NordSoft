from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from account.forms import RegistrationForm, LoginForm
from .tasks import send_password

from random import random
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            send_password.delay(user.id)
            return render(request, 'account/register_done.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('account:login')


# Регистрация пользователя с отправкой подтверждающей ссылки.
# def registration_view(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             email_subject = 'Activate Your Account'
#             message = render_to_string('account/activate_account.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(email_subject, message, to=[to_email])
#             email.send()
#             return render(request, 'account/register_done.html', {'form': form})
#     else:
#         form = RegistrationForm()
#     return render(request, 'account/register.html', {'form': form})


# def activate_account(request, uidb64):
#     try:
#         uid = force_bytes(urlsafe_base64_decode(uidb64))
#         user = Account.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
#         user = None
#     if user is not None:
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return redirect('home')
#     else:
#         return HttpResponse('Ссылка для активации недействительна!')



