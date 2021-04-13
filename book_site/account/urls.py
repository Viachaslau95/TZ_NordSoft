from django.urls import path
from .views import RegistrationView, AuthenticationForm, LogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', AuthenticationForm.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),




]
