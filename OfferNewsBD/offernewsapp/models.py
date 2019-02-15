from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime


# Coding By Abdullah on 8/10/2018

class Profile (models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phn = models.CharField(db_index=True, max_length=11, unique=True)
    infoUpdatedOn = models.DateField(auto_now=True, auto_now_add=False)
    createdOn = models.DateField(auto_now=False, auto_now_add=True)
    userPic = models.ImageField(default='default', upload_to='pro_pics', blank=True)
    #slug = models.SlugField(max_length=80, unique=True, blank=False)

    def __str__(self):
        return self.name.username



class Company (models.Model):
    comName = models.CharField(db_index=True, max_length=60, blank=False)
    comDes = models.TextField()
    comAddress = models.TextField(max_length=200)
    comPhn = models.CharField(max_length=11)
    comWeb = models.CharField(max_length=42, blank=True)
    comImage = models.ImageField(default='default.jpg', upload_to='com_pics', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
    NEW = 'NEW'
    HOT = 'HOT'
    EXPIRED = 'EXPIRED'

    Badge_Type = (
        (NEW, 'New'),
        (HOT, 'Hot'),
        (EXPIRED, 'Expired'),
    )

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
    badgeType = models.CharField(max_length=7, choices=Badge_Type, default=NEW)
    Amount = models.CharField(max_length=200)
    postImage = models.ImageField(default='default.jpg', upload_to='post_pics', blank=True)
    isActive = models.BooleanField(default=True)
    isFeatured = models.BooleanField(default=False)
    goingUrl = models.URLField()
    postedOn = models.DateTimeField(auto_now=False, auto_now_add=True)
    expiredOn = models.DateField()
    editedOn = models.DateTimeField(auto_now=True, auto_now_add=False)
    # slug = models.SlugField(max_length=80, unique=True, blank=False)
    branch = models.ForeignKey(Branch, on_delete=None)

    def __str__(self):
        return self.title



class Coupon(models.Model):
    postId = models.OneToOneField(Post, on_delete=models.CASCADE)
    couponCode = models.CharField(db_index=True, max_length=50)

    def __str__(self):
        return self.couponCode


class PostFeaturePricing(models.Model):
    COVER_BIG = 'Cover Big'
    COVER_SMALL = 'Cover Small'
    FIRST_PAGE = 'First Page'

    Position_Type = (
        (COVER_BIG, 'Cover_Big'),
        (COVER_SMALL, 'Cover_Small'),
        (FIRST_PAGE, 'First_Page'),
    )
    position = models.CharField(max_length=15, choices=Position_Type, default=FIRST_PAGE)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position




class ComFeaturePricing(models.Model):
    COM_PAGE = 'Company Page'
    FIRST_PAGE = 'First Page'

    Position_Type = (
        (COM_PAGE, 'Com_Page'),
        (FIRST_PAGE, 'First_Page'),
    )
    position = models.CharField(max_length=15, choices=Position_Type, default=FIRST_PAGE)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position




class FeaturedPost(models.Model):
    COVER_BIG = 'Cover Big'
    COVER_SMALL = 'Cover Small'
    FIRST_PAGE = 'First Page'

    Position_Type = (
        (COVER_BIG, 'Cover_Big'),
        (COVER_SMALL, 'Cover_Small'),
        (FIRST_PAGE, 'First_Page'),
    )
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postId')
    position = models.CharField(max_length=15, choices=Position_Type, default=FIRST_PAGE)
    featuredExpireDate = models.DateField()
    featuredDate = models.DateField(auto_now=False, auto_now_add=True)
    isActive = models.BooleanField(db_index=True, default=True)

    def __str__(self):
        return self.position

    @property
    def PriceCalculation (self, featuredDate, featuredExpireDate):
        delta = featuredExpireDate - featuredDate
        price = delta.days * PostFeaturePricing.price
        return price



class FeaturedCom(models.Model):
    COM_PAGE = 'Company Page'
    FIRST_PAGE = 'First Page'

    Position_Type = (
        (COM_PAGE, 'Com_Page'),
        (FIRST_PAGE, 'First_Page'),
    )
    comId = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=15, choices=Position_Type, default=FIRST_PAGE)
    featuredExpireDate = models.DateField()
    featuredDate = models.DateField(auto_now=False, auto_now_add=True)
    isActive = models.BooleanField(db_index=True, default=True)
    priceId = models.ForeignKey(ComFeaturePricing, on_delete=models.CASCADE)

    def __str__(self):
        return self.position

    @property
    def PriceCalculation(self, featuredDate, featuredExpireDate):
        delta = featuredExpireDate - featuredDate
        price = delta.days * ComFeaturePricing.price
        return price



class ExternalAdPricing(models.Model):
    FRONT_PAGE = 'Front Page'
    POPUP = 'Popup'

    Position_Type = (
        (POPUP, 'Popup'),
        (FRONT_PAGE, 'Front_Page'),
    )
    position = models.CharField(max_length=15, choices=Position_Type, default=FRONT_PAGE)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position



class ExternalAd(models.Model):
    FRONT_PAGE = 'Front Page'
    POPUP = 'Popup'

    Position_Type = (
        (POPUP, 'Popup'),
        (FRONT_PAGE, 'Front_Page'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(db_index=True, max_length=100)
    position = models.CharField(max_length=15, choices=Position_Type, default=FRONT_PAGE)
    featuredExpireDate = models.DateField()
    featuredDate = models.DateField(auto_now=False, auto_now_add=True)
    isActive = models.BooleanField(db_index=True, default=True)

    def __str__(self):
        return self.title

    @property
    def PriceCalculation(self, featuredDate, featuredExpireDate):
        delta = featuredExpireDate - featuredDate
        price = delta.days * ExternalAdPricing.price
        return price

class Meta(models.Model):
    title = models.CharField(max_length=200)
    keyword = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=30,blank=False)
    phn = models.CharField(db_index=True, blank=False, max_length=11, default=1)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=250)
    sendOn = models.DateTimeField(db_index=True, auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
