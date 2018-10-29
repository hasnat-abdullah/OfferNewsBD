from django.conf.urls import url
from . import views
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('user/<name>', views.getauthor, name="Dashboard"),
    path('login/', views.getsignin, name="login"),
    path('signup/', views.getsignup, name="signup"),
    path('logout', views.getlogout, name="logout"),
    path('about/', views.getaboutus, name="about"),
    path('contact/', views.getcontact, name="contact"),
    path('store/', views.getstore, name="store"),
    path('submit/', views.getsubmition, name="submit"),
    path('deal/<int:id>', views.getsingledeal, name="deal"),
    path('coupon/<int:id>', views.getsinglecoupon, name="coupon"),
    path('<name>', views.getcategory, name="category"),
    path('offer/', views.getalloffer, name="offer"),
    path('store/<int:id>', views.getsinglestore, name="singleStore"),
]