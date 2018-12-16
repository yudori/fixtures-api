from django.urls import path
from rest_framework.authtoken import views as token_views

from accounts.v1 import views as account_views


urlpatterns = [
    path('login/', token_views.obtain_auth_token, name='login'),
    path('register/', account_views.RegisterVeiw.as_view(), name='register'),
]
