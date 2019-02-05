from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Profile, Company, Branch, Category, Post, Coupon, Contact, FeaturedPost,FeaturedCom, PostFeaturePricing, ComFeaturePricing, Meta, ExternalAdPricing, ExternalAd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import ContactForm, SignUpForm, PostForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import resolve


# from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    post = Post.objects.filter(isActive=True).order_by('-postedOn')
    featuredpost = Post.objects.filter(isActive=True, isFeatured=True).order_by('-postedOn')
    couponpost = FeaturedPost.objects.filter(isActive=True).order_by('?')
    store = Company.objects.all().order_by('-createdOn')
    context = {
        'post': post,
        'store': store,
        'featuredpost': featuredpost,
        'couponpost': couponpost,
    }
    return render(request, "index.html", context)


def getauthor(request, name):
    context = {
        'username': name
    }
    return render(request, "dashboard.html", context)


def getcategory(request, name):
    cat = get_object_or_404(Category, catName=name)
    post = Post.objects.filter(category=cat.id)
    context = {
        'post': post,
        'cat': cat,
    }
    return render(request, "category.html", context)


def getalloffer(request):
    post = Post.objects.filter(isActive=True).order_by('-postedOn')
    coupon = Post.objects.filter(isActive=True, offerType='C').order_by('-postOn')
    deal = Post.objects.filter(isActive=True, offerType='D').order_by('-postOn')
    cat = Category.objects.all()
    # ==========Search==========
    search = request.GET.get('q')
    if search:
        post=post.filter(
            Q(title__icontains=search) |
            Q(description__icontains= search)
        )
    # ==========Paginator==========
    paginator = Paginator(post, 12)  # Show 12 contacts per page

    page = request.GET.get('page')
    totalArticle = paginator.get_page(page)
    context = {
        'post': totalArticle,
        'coupon': coupon,
        'deal': deal,
        'cat': cat,
    }
    return render(request, "category.html", context)


def getaboutus(request):
    return render(request, "about-us.html")


def getcontact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name')
        phn = request.POST.get('phn')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = form(name=name, phn=phn, subject=subject, message=message, )
        form.save()
        messages.add_message(request, messages.SUCCESS, "Your message sent successfully.")

    return render(request, "contact.html", {"form": form})


def getsinglecoupon(request, id):
    coupon = get_object_or_404(Post, pk=id)
    related = Post.objects.filter(category=coupon.category).exclude(id=id)[:4]
    context = {
        'coupon': coupon,
        'related': related,
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
    if request.user.is_authenticated:
        getUser = name=request.user.id
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = getUser
            instance.save()
            return redirect('index')
        return render(request, "submit-coupon.html", {"form": form})
    else:
        return redirect('login')


# Login Function
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
                messages.add_message(request, messages.ERROR, "Username or Password Mismatch")

    return render(request, "signin.html")


def getsignup(request):
    if request.method == "GET":
        form = SignUpForm(request.POST or None)
        return render(request, "signup.html", {"form": form})
    else:
        form = SignUpForm(request.POST)
        first_name = request.POST.get("first_name")
        first_name=first_name.lower()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_active = True
            usr = User.objects.all()
            i = 0
            for u in usr:
                if u.username == first_name + str(i) or u.username == first_name:
                    i = i + 1
                else:
                    pass
            instance.username = first_name + str(i)
            instance.save()
            return HttpResponse("You are registered with username: "+first_name+str(i)+". Click <a href='/login'>here</a> to login")
        else:
            return redirect("signup")


def getlogout(request):
    logout(request)
    return redirect('index')
