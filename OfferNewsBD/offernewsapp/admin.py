from django.contrib import admin
from .models import User, Company, Branch, Category, Post, Coupon, Contact, Featured, FeaturePricing, AdPricing, FeaturedPosition, Meta, Advertise, Transaction

# Register your models here.

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Category)
admin.site.register(Coupon)
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Featured)
admin.site.register(FeaturePricing)
admin.site.register(AdPricing)
admin.site.register(FeaturedPosition)
admin.site.register(Meta)
admin.site.register(Advertise)
admin.site.register(Transaction)
