from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from .models import Profile, Company, Branch, Category, Post, Coupon, Contact, Featured, FeaturePricing, AdPricing, FeaturedPosition, Meta, Advertise
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from .forms import CreateForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    post = Post.objects.filter(isActive=True).order_by('-postedOn')
    featuredpost = Post.objects.filter(isActive=True, isFeatured=True).order_by('-postedOn')
    couponpost = Featured.objects.filter(isActive=True).order_by('?')
    store = Company.objects.all().order_by('-createdOn')
    context={
        'post':post,
        'store':store,
        'featuredpost':featuredpost,
        'couponpost': couponpost,
    }
    return render(request, "index.html", context)


def getauthor(request, name):
    return render(request, "dashboard.html")


def getcategory(request, name):
    cat=get_object_or_404(Category, catName=name)
    post=Post.objects.filter(category=cat.id)
    context = {
        'post': post,
        'cat':cat,
    }
    return render(request, "category.html",context)


def getalloffer(request):
    post = Post.objects.filter(isActive=True).order_by('-postedOn')[:18]
    coupon= Post.objects.filter(isActive=True, offerType='C' ).order_by('-postOn')
    deal = Post.objects.filter(isActive=True, offerType='D').order_by('-postOn')
    cat = Category.objects.all()

    # ==========Paginator==========
    paginator = Paginator(post, 12)  # Show 12 contacts per page

    page = request.GET.get('page')
    totalArticle = paginator.get_page(page)
    context = {
        'post': totalArticle,
        'coupon':coupon,
        'deal':deal,
        'cat':cat,
    }
    return render(request, "category.html",context)


def getaboutus(request):
    return render(request, "about-us.html")


def getcontact(request):
    return render(request, "contact.html")


def getsinglecoupon(request, id):
    coupon=get_object_or_404(Post, pk=id)
    related = Post.objects.filter(category=coupon.category).exclude(id=id)[:4]
    context={
        'coupon':coupon,
        'related':related,
    }
    return render(request, "single-coupon-code.html", context)


def getsingledeal(request, id):
    deal = get_object_or_404(Post, pk=id)
    related = Post.objects.filter(category=deal.category).exclude(id=id)[:4]
    context = {
        'deal': deal,
        'related': related,
    }
    return render(request, "single-coupon-sale.html", context)


def getsinglestore(request, id):
    return render(request, "single-store.html")


def getstore(request):
    return render(request, "stores.html")


def getsubmition(request):
    #form = CreateForm()
    return render(request, "submit-coupon.html")

#Login Function
def getsignin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('password')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
            else:
                messages.add_message(request,messages.ERROR, "Username or Password Mismatch")

    return render(request, "signin.html")


def getsignup(request):
    # form = UserCreationForm(request.POST or None)
    return render(request, "signup.html")


def getlogout(request):
    logout(request)
    return redirect('index')


