from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPage, name='loginpage'),
    path('learnorshop', views.page2, name='learnorshop')
]
