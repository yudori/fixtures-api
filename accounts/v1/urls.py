from django.urls import path

from accounts.v1 import views as account_views


app_name = 'accounts'

urlpatterns = [
    path('login/', account_views.LoginView.as_view(), name='login'),
    path('register/', account_views.RegisterVeiw.as_view(), name='register'),
]
