from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
]