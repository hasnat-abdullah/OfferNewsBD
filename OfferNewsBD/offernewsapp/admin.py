from django.contrib import admin
from .models import Profile, Company, Branch, Category, Post, Coupon, Contact, Featured, FeaturePricing, AdPricing, FeaturedPosition, Meta, Advertise

# Register your models here.


class ProfileModel(admin.ModelAdmin):
    list_display = ["__str__","phn","email"]
    search_fields = ["__str__"]

    class Meta:
        Model = Profile

admin.site.register(Profile, ProfileModel)


class CompanyModel(admin.ModelAdmin):
    list_display = ["__str__", "comPhn", "AuthorId"]
    search_fields = ["__str__"]

    class Meta:
        Model = Company

admin.site.register(Company, CompanyModel)


class BranchModel(admin.ModelAdmin):
    list_display = ["__str__", "comId"]
    search_fields = ["__str__"]

    class Meta:
        Model = Branch
admin.site.register(Branch, BranchModel)


class CategoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Category
admin.site.register(Category, CategoryModel)


class CouponModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Coupon
admin.site.register(Coupon, CouponModel)


class PostModel(admin.ModelAdmin):
    list_display = ["__str__", "postedOn", "comName", "category", "offerType", "isActive", "expiredOn",]
    search_fields = ["__str__"]
    list_filter = ["postedOn", "category"]
    list_per_page = 30

    class Meta:
        Model = Post
admin.site.register(Post, PostModel)


class ContactModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Contact
admin.site.register(Contact, ContactModel)


class FeaturedModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Featured
admin.site.register(Featured, FeaturedModel)


class FeaturePricingModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = FeaturePricing
admin.site.register(FeaturePricing, FeaturePricingModel)


class AdPricingModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = AdPricing
admin.site.register(AdPricing, AdPricingModel)


class FeaturedPositionModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]

    class Meta:
        Model = FeaturedPosition
admin.site.register(FeaturedPosition, FeaturedPositionModel)


class MetaModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Meta
admin.site.register(Meta, MetaModel)


class AdvertiseModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Advertise
admin.site.register(Advertise, AdvertiseModel)
