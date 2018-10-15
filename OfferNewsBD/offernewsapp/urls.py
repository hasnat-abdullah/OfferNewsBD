from django.conf.urls import url
from . import views
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('user/<name>', views.getauthor, name="Dashboard"),
    path('signin/', views.getsignin, name="signin"),
    path('signup/', views.getsignup, name="signup"),
    path('about/', views.getaboutus, name="about"),
    path('contact/', views.getcontact, name="contact"),
    path('store/', views.getstore, name="store"),
    path('submit/', views.getsubmition, name="submit"),
    path('deal/<int:id>', views.getsingledeal, name="deal"),
    path('coupon/<int:id>', views.getsinglecoupon, name="coupon"),
    path('offer/', views.getcategory, name="offer"),
    path('store/<int:id>', views.getsinglestore, name="singleStore"),
]