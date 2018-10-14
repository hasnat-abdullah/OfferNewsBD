from django.db import models
from django.contrib.auth.models import User


# Coding By Abdullah on 8/10/2018

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phn = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    infoUpdatedOn = models.DateField(auto_now=True, auto_now_add=False)
    createdOn = models.DateField(auto_now=False, auto_now_add=True)
    userPic = models.ImageField(default='defaultProPic.jpg', upload_to='pro_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Company (models.Model):
    comName = models.CharField(max_length=60, blank=False)
    comDes = models.TextField()
    comAddress = models.TextField(max_length=200)
    comPhn = models.CharField(max_length=12)
    comWeb = models.CharField(max_length=50, blank=True)
    comImage = models.ImageField(default='defaultProPic.jpg', upload_to='com_pics', blank=True)
    AuthorId = models.ForeignKey(User, on_delete=models.CASCADE)
    infoUpdatedOn = models.DateField(auto_now=True, auto_now_add=False)
    createdOn = models.DateField(auto_now=False, auto_now_add=True)
    isVerified = models.BooleanField(blank=False)

    def __str__(self):
        return self.comName


class Branch(models.Model):
    branchName = models.CharField(max_length=20)
    managerId = models.ForeignKey(User, on_delete=models.CASCADE)
    branchAddress = models.TextField(max_length=200)
    branchPhn = models.CharField(max_length=12)
    comId = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.branchName


class Category(models.Model):
    catName = models.CharField(max_length=20)
    catIcon = models.FileField(default='defaultProPic.jpg', upload_to='cat_pics', blank=True)

    def __str__(self):
        return self.catName


class Post(models.Model):
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
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comName = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dealType = models.CharField(max_length=1, choices=Deal_Type, default=DEAL)
    AmountType = models.CharField(max_length=1, choices=Amount_Type, default=PERCENTAGE)
    Amount = models.CharField(max_length=200)
    postImage = models.ImageField(default='default.jpg', upload_to='post_pics', blank=True)
    isActive = models.BooleanField(default=True)
    isFeatured = models.BooleanField(default=False)
    goingUrl = models.URLField()
    postedOn = models.DateTimeField(auto_now=False, auto_now_add=True)
    expiredOn = models.DateTimeField()
    editedOn = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class Coupon(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    couponCode = models.CharField(max_length=50)

    def __str__(self):
        return self.couponCode


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sendOn = models.DateTimeField(auto_now=False, auto_now_add=True)

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
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    featuredExpireDate = models.DateField()
    featuredDate = models.DateField(auto_now=False, auto_now_add=True)
    isActive = models.BooleanField(default=True)
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
