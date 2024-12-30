from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPage, name='loginpage'),
    path('learnorshop', views.page2, name='learnorshop'),
    path('elearnhome',views.ehome, name="elearnhome"),
    path('pricing', views.pricing, name='pricing'),
    path('shop', views.shop, name='shop')
]
