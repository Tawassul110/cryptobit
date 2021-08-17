from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trade/', views.trade, name='trade'),
    path('market/', views.market, name='market'),
    path('visacard/', views.visacard, name='visacard'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('details/', views.details, name='details')
]
