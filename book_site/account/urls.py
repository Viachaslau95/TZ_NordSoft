from django.urls import path
from .views import registration_view, user_login, user_logout, activate_account

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('activate/<uidb64>', activate_account, name='activate'),

]
