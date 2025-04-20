from django.urls import path
from apps.users.views import LoginView


urlpatterns = [
    path('auth/login', LoginView.as_view(), name='auth_login')
]