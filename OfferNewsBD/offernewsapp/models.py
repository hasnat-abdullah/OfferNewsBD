from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime


# Coding By Abdullah on 8/10/2018

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phn = models.CharField(db_index=True, max_length=11, unique=True)
    infoUpdatedOn = models.DateField(auto_now=True, auto_now_add=False)
    createdOn = models.DateField(auto_now=False, auto_now_add=True)
    userPic = models.ImageField(default='default', upload_to='pro_pics', blank=True)
    #slug = models.SlugField(max_length=80, unique=True, blank=False)

    def __str__(self):
        return f'{self.user.username} Profile'


class UserAddress (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.city} UserAddress'


class UserEmail (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(db_index=True, unique=True)

    def __str__(self):
        return f'{self.user.email} UserEmail'


class Company (models.Model):
    comName = models.CharField(db_index=True, max_length=60, blank=False)
    comDes = models.TextField()
    comAddress = models.TextField(max_length=200)
    comPhn = models.CharField(max_length=11)
    comWeb = models.CharField(max_length=42, blank=True)
    comImage = models.ImageField(default='default.jpg', upload_to='com_pics', blank=True)
    AuthorId = models.ForeignKey(User, on_delete=models.CASCADE)
    infoUpdatedOn = models.DateField(auto_now=True, auto_now_add=False)
    createdOn = models.DateField(auto_now=False, auto_now_add=True)
    isVerified = models.BooleanField(blank=False)
    #slug = models.SlugField(max_length=80, unique=True, blank=False)

    def __str__(self):
        return self.comName


class Branch(models.Model):
    branchName = models.CharField(max_length=20)
    managerId = models.ForeignKey(User, on_delete=models.CASCADE)
    branchAddress = models.TextField(max_length=200)
    branchPhn = models.CharField(max_length=11)
    comId = models.ForeignKey(Company, on_delete=models.CASCADE)
    #slug = models.SlugField(max_length=80, unique=True, blank=False, default=True)
    def __str__(self):
        return self.branchName


class Category(models.Model):
    catName = models.CharField(max_length=20)
    catIcon = models.FileField(default='default.jpg', upload_to='cat_pics', blank=True)

    def __str__(self):
        return self.catName


class Post(models.Model):
    DEAL = 'D'
    COUPON = 'C'
    PERCENTAGE = 'P'
    TAKA = 'T'
    GIFT = 'G'

    Offer_Type = (
        (DEAL, 'Deal'),
        (COUPON, 'Coupon'),
    )
    Amount_Type = (
        (PERCENTAGE, 'Percentage'),
        (TAKA, 'Taka'),
        (GIFT, 'Gift'),
    )
    title = models.CharField(db_index=True, max_length=200)
    description = models.TextField()
    author = models.ForeignKey( User, db_index=True, on_delete=models.CASCADE)
    comName = models.ForeignKey(Company, db_index=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, db_index=True, on_delete=models.CASCADE)
    offerType = models.CharField(max_length=1, choices=Offer_Type, default=DEAL)
    AmountType = models.CharField(max_length=1, choices=Amount_Type, default=PERCENTAGE)
    Amount = models.CharField(max_length=200)
    postImage = models.ImageField(default='default.jpg', upload_to='post_pics', blank=True)
    isActive = models.BooleanField(default=True)
    isFeatured = models.BooleanField(default=False)
    goingUrl = models.URLField()
    postedOn = models.DateTimeField(auto_now=False, auto_now_add=True)
    expiredOn = models.DateTimeField()
    editedOn = models.DateTimeField(auto_now=True, auto_now_add=False)
    # slug = models.SlugField(max_length=80, unique=True, blank=False)

    def __str__(self):
        return self.title


class Coupon(models.Model):
    postId = models.OneToOneField(Post, on_delete=models.CASCADE)
    couponCode = models.CharField(db_index=True, max_length=50)

    def __str__(self):
        return self.couponCode


class Contact(models.Model):
    name = models.CharField(max_length=30,blank=False)
    phn = models.CharField(db_index=True, blank=False, max_length=11, default=1)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=250)
    sendOn = models.DateTimeField(db_index=True, auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Featured(models.Model):
    FEATURE_POST = 'FP'
    FEATURE_COMPANY = 'FC'

    Featured_Type = (
        (FEATURE_POST, 'Feature_Post'),
        (FEATURE_COMPANY, 'Feature_Company'),
    )
    featuredType = models.CharField(max_length=2, choices=Featured_Type, default=FEATURE_POST)
    postId = models.OneToOneField(Post, db_index=True, on_delete=models.CASCADE)
    featuredExpireDate = models.DateField()
    featuredDate = models.DateField(auto_now=False, auto_now_add=True)
    isActive = models.BooleanField(db_index=True, default=True)
    # price = models.ForeignKey(Pricing, on_delete=models.CASCADE)

    def __str__(self):
        return self.featuredType


class FeaturePricing(models.Model):
    FEATURE_POST = 'FP'
    FEATURE_COMPANY = 'FC'

    Featured_Type = (
        (FEATURE_POST, 'Feature_Post'),
        (FEATURE_COMPANY, 'Feature_Company'),

    )
    durationType = models.CharField(max_length=20)
    featuredType = models.CharField(max_length=2, choices=Featured_Type, default=FEATURE_POST)
    # position = models.ForeignKey(FeaturedPosition, on_delete=models.CASCADE())
    priceAmount = models.PositiveIntegerField()

    def __str__(self):
        return self.featuredType


class AdPricing(models.Model):
    durationType = models.CharField(max_length=20)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.durationType


class FeaturedPosition(models.Model):
    COVER = 'C'
    FIRST_PAGE = 'F'
    POPUP = 'P'

    Position_Type = (
        (COVER, 'Cover'),
        (FIRST_PAGE, 'First_Page'),
        (POPUP, 'Popup'),
    )
    position = models.CharField(max_length=1, choices=Position_Type, default=FIRST_PAGE)

    def __str__(self):
        return self.position


class Meta(models.Model):
    title = models.CharField(max_length=200)
    keyword = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Advertise(models.Model):
    advertiser = models.ForeignKey(User, on_delete=models.CASCADE)
    durationType = models.CharField(max_length=20)
    adExpireDate = models.DateField()
    adDate = models.DateField(auto_now=False, auto_now_add=True)
    isActive = models.BooleanField(default=True)
    price = models.ForeignKey(AdPricing, on_delete=models.CASCADE)

    def __str__(self):
        return self.advertiser
