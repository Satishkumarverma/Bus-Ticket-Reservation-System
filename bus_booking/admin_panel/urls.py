from django.urls import path
from admin_panel import views

urlpatterns = [
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('adminsingup/', views.adminsingup, name='adminsingup'),
    path('adminforgetpassword/', views.adminforgetpassword, name='adminforgetpassword'),
    path('adminaddbus/', views.adminaddbus, name='adminaddbus'),
    path('adminupdate/<busnumber>', views.adminupdate, name='adminupdate'),
    path('admindeletebus/<busnumber>', views.admindeletebus, name='admindeletebus'),
    path('adminbooking/', views.adminbooking, name='adminbooking'),
    path('statusbooked/<int:b_id>', views.statusbooked, name='statusbooked'),
    path('statusrejected/<int:b_id>', views.statusrejected, name='statusrejected'),
]