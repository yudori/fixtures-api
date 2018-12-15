from django.conf.urls import url, include
from django.urls import path

from accounts.v1 import views as views_v1


urlpatterns = [
    url(r'', include('rest_framework.urls')),
    path('register/', views_v1.RegisterVeiw.as_view(), name='register'),
]
