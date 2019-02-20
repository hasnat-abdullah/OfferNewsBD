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
    path('offer_form/', views.getsubmition, name="offer_form"),
    path('deal/<slug:slug>', views.getsingledeal, name="deal"),
    path('coupon/<slug:slug>', views.getsinglecoupon, name="coupon"),
    path('category/<slug:slug>', views.getcategory, name="category"),
    path('offer/', views.getalloffer, name="offer"),
    path('store/<slug:slug>', views.getsinglestore, name="singleStore"),
    path('ajx_profile_info/', views.ajxuserinfo, name="ajx_user_profile_info"),
    path('ajx_user_edit_profile/', views.ajxusereditprofile, name="ajx_user_edit_profile"),
    path('ajx_user_offer_info/', views.ajxuserofferinfo, name="ajx_user_offer_info"),
    path('ajx_user_sponsor_info/', views.ajxusersponsorinfo, name="ajx_user_sponsor_info"),
    path('ajx_user_company_info/', views.ajxusercompanyinfo, name="ajx_user_company_info"),
]