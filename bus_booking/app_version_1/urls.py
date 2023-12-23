from django.contrib import admin
from django.urls import path
from app_version_1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup_/', views.signup_, name='signuppage'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('bookings/', views.bookings, name='bookings'),
    path('about/', views.about, name='about'),
    path('bussearch/', views.bussearch, name='bussearch'),
    path('bookbus/', views.bookbus, name='bookbus'),
    path('payment/', views.payment, name='payment'),
    path('transaction/', views.transaction, name='transaction'),
]
