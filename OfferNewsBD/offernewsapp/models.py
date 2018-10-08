from django.db import models
from django.contrib.auth.models import User
#
#Coding By Abdullah on 8/10/2018

class User(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    phn = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    lastLogin = models.DateTimeField()
    infoUpdatedOn = models.DateField(auto_now=True,auto_now_add=False)
    createdOn = models.DateField(auto_now=False, auto_now_add=True)
    userPic = models.ImageField()
    pas = models.TextField(max_length=40)


class Company(models.Model):
    comId = models.PositiveIntegerField(primary_key=True)
    comName = models.CharField(max_length=60,blank=False)
    comDes = models.TextField()
    comAddress = models.TextField(max_length=200)
    comPhn = models.CharField(max_length=12)
    comWeb = models.CharField(blank=True)
    comImage = models.ImageField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    infoUpdatedOn = models.DateField(auto_now=True, auto_now_add=False)
    createdOn = models.DateField(auto_now=False, auto_now_add=True)
    isVerified = models.BooleanField(blank=False)


class Branch (models.Model):
    branchId = models.PositiveIntegerField(primary_key=True)
    managerId=models.ForeignKey(User, on_delete=models.CASCADE)
    comAddress = models.TextField(max_length=200)
    comPhn = models.CharField(max_length=12)
    comId = models.ForeignKey(Company,on_delete=models.CASCADE)


class Category (models.Model):
    catId = models.PositiveIntegerField(primary_key=True)
    catName = models.CharField(max_length=20)


class Post (models.Model):
    DEAL = 'D'
    COUPON = 'C'
    PERCENTAGE = 'P'
    TAKA = 'T'
    GIFT = 'G'

    Deal_Type = (
        (DEAL, 'Deal'),
        (COUPON, 'Coupon'),
    )
    Amount_Type = (
        (PERCENTAGE, 'Percentage'),
        (TAKA, 'Taka'),
        (GIFT, 'Gift'),
    )
    postId = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=40)
    comName = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dealType = models.CharField(max_length=1, choices=Deal_Type, default=DEAL)
    AmountType = models.CharField(max_length=1, choices=Amount_Type, default=PERCENTAGE)
    Amount = models.CharField(max_length=200)
    postImage = models.ImageField()
    isActive = models.BooleanField()
    postedOn = models.DateTimeField(auto_now=False, auto_now_add=True)
    expiredOn = models.DateTimeField()
    editedOn = models.DateTimeField(auto_now=True, auto_now_add=False)


class Coupon (models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    couponCode = models.CharField(max_length=50)


class Contact (models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sendOn = models.DateTimeField(auto_now=False, auto_now_add=True)

