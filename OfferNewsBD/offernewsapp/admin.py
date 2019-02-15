from django.contrib import admin
from .models import Profile, Company, Branch, Category, Post, Coupon, Contact, FeaturedPost,FeaturedCom, PostFeaturePricing, ComFeaturePricing, Meta, ExternalAdPricing, ExternalAd

# Register your models here.

class ProfileModel(admin.ModelAdmin):
    list_display = ["__str__","phn"]
    search_fields = ["__str__"]

    class Meta:
        Model = Profile


admin.site.register(Profile, ProfileModel)


class CompanyModel(admin.ModelAdmin):
    list_display = ["__str__", "comPhn", "author"]
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
    list_display = ["__str__","postId"]
    search_fields = ["__str__"]

    class Meta:
        Model = Coupon


admin.site.register(Coupon, CouponModel)


class PostModel(admin.ModelAdmin):
    list_display = ["__str__", "postedOn", "comName","author", "category", "offerType", "isActive", "expiredOn",]
    search_fields = ["__str__"]
    list_filter = ["postedOn", "category"]
    list_per_page = 30

    class Meta:
        Model = Post


admin.site.register(Post, PostModel)


class ContactModel(admin.ModelAdmin):
    list_display = ["__str__", "phn", "subject", "sendOn"]
    search_fields = ["__str__"]

    class Meta:
        Model = Contact


admin.site.register(Contact, ContactModel)


class FeaturedPostModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = FeaturedPost


admin.site.register(FeaturedPost, FeaturedPostModel)



class FeaturedComModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = FeaturedCom


admin.site.register(FeaturedCom, FeaturedComModel)



class PostFeaturePricingModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = PostFeaturePricing

admin.site.register(PostFeaturePricing, PostFeaturePricingModel)



class ComFeaturePricingModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = ComFeaturePricing

admin.site.register(ComFeaturePricing, ComFeaturePricingModel)



class ExternalAdPricingModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = ExternalAdPricing


admin.site.register(ExternalAdPricing, ExternalAdPricingModel)


class ExternalAdModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = ExternalAd


admin.site.register(ExternalAd, ExternalAdModel)



class MetaModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Meta


admin.site.register(Meta, MetaModel)