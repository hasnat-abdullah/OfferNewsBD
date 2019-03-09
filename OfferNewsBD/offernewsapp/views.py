from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Profile, Company, Branch, Category, Post, Coupon, Contact, FeaturedPost,FeaturedCom, PostFeaturePricing, ComFeaturePricing, Meta, ExternalAdPricing, ExternalAd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import ContactForm, SignUpForm, PostForm, CouponForm, FeaturedPostForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import resolve


# from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# ==========index Page===========
def index(request):
    post = Post.objects.filter(isActive=True).order_by('-postedOn')
    featuredpost = post.filter(isFeatured=True).order_by('?')
    coverPost=FeaturedPost.objects.filter(isActive=True, position='Cover Big').prefetch_related('postId').order_by('?')[:3]
    coverSmallPost = FeaturedPost.objects.filter(isActive=True, position='Cover Small').prefetch_related('postId').order_by('?')[:2]
    store = FeaturedCom.objects.filter(isActive=True,position='First Page').prefetch_related('comId').order_by('?')[:4]
    context = {
        'post': post,
        'store': store,
        'featuredpost': featuredpost,
        'coverPost': coverPost,
        'coverSmallPost': coverSmallPost,
    }
    return render(request, "index.html", context)

# ==========User Info AJX===========
def ajxuserinfo(request):
    if request.user.is_authenticated:
        return render(request, "ajx-user-info.html")
    return redirect('login')

# ==========User Info Edit AJX===========
def ajxusereditprofile(request):
    if request.user.is_authenticated:
        form = SignUpForm(request.POST or None)
        return render(request, "ajx-user-edit-profile.html", {"form": form})
    return redirect('login')

# ==========User Companies Info AJX===========
def ajxusercompanyinfo(request):
    if request.user.is_authenticated:
        return render(request, "ajx-user-company-info.html")
    return redirect('login')

# ==========User Offers Info AJX===========
def ajxuserofferinfo(request):
    if request.user.is_authenticated:
        return render(request, "ajx-user-offer-info.html")
    return redirect('login')

# ==========User Sponsors Info AJX===========
def ajxusersponsorinfo(request):
    if request.user.is_authenticated:
        return render(request, "ajx-user-sponsor-info.html")
    return redirect('login')

# ==========Author Page===========
def getauthor(request, name):
    if request.user.is_authenticated:
        u=get_object_or_404(User, id=request.user.id)
        if u.username==name:
            context = {
                'user': u
            }
            return render(request, "dashboard.html", context)
        else:
            return redirect('category')
    return redirect('index')

# ==========Category page Page===========
def getcategory(request, slug):
    cat = Category.objects.all()
    getCat=get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=getCat.id,isActive=True).order_by('-postedOn')
    coupon = post.filter(isActive=True, offerType='C')
    deal = post.filter(isActive=True, offerType='D')

    # ==========Paginator==========
    paginator = Paginator(post, 15)  # Show 15 contacts per page

    page = request.GET.get('page')
    totalArticle = paginator.get_page(page)

    context = {
        'post': totalArticle,
        'cat': cat,
        'coupon': coupon,
        'deal': deal,
    }
    return render(request, "category.html", context)

# ==========All Offer Page===========
def getalloffer(request):
    post = Post.objects.filter(isActive=True).order_by('-postedOn')
    coupon = post.filter( offerType='C')
    deal = post.filter( offerType='D')
    cat = Category.objects.all()
    # ==========Search==========
    search = request.GET.get('q')
    if search:
        post=post.filter(
            Q(title__icontains=search) |
            Q(description__icontains= search)
        )

    # ==========Paginator==========
    paginator = Paginator(post, 15)  # Show 15 contacts per page

    page = request.GET.get('page')
    totalArticle = paginator.get_page(page)
    context = {
        'post': totalArticle,
        'coupon': coupon,
        'deal': deal,
        'cat': cat,
    }
    return render(request, "category.html", context)

# ==========About Us Page===========
def getaboutus(request):
    return render(request, "about-us.html")

# ==========Contact Page===========
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

# ==========Single Coupon Page===========
def getsinglecoupon(request, slug):
    coupon = get_object_or_404(Post, slug=slug)
    code=Coupon.objects.get(postId=coupon.id)
    related = Post.objects.filter(category=coupon.category).exclude(id=coupon.id)[:4]
    context = {
        'coupon': coupon,
        'related': related,
        'code': code,
    }
    return render(request, "single-coupon-code.html", context)

# ==========Single Deal Page===========
def getsingledeal(request, slug):
    deal = get_object_or_404(Post, slug=slug)
    related = Post.objects.filter(category=deal.category).exclude(id=deal.id)[:4]
    context = {
        'deal': deal,
        'related': related,
    }
    return render(request, "single-coupon-sale.html", context)

# ==========Single store Page===========
def getsinglestore(request, slug):
    company=get_object_or_404(Company, slug=slug)
    post=Post.objects.filter(comName=company.id).order_by('-postedOn')

    #========Paginator==========
    paginator = Paginator(post, 8)  # Show 8 contacts per page
    page = request.GET.get('page')
    totalArticle = paginator.get_page(page)
    context={
        'company':company,
        'post':totalArticle,
    }
    return render(request, "single-store.html", context)

# ==========All Store Page===========
def getstore(request):
    store = Company.objects.all().order_by('-createdOn')
    featuredStoreCom = FeaturedCom.objects.filter(isActive=True,position='Company Page').prefetch_related('comId').order_by('?')[:4]

    # ==========Paginator==========
    paginator = Paginator(store, 12)  # Show 15 contacts per page

    page = request.GET.get('page')
    totalStore = paginator.get_page(page)
    context = {
        'store': totalStore,
        'featuredStoreComPage': featuredStoreCom,
    }
    return render(request, "stores.html",context)

# ==========Offer Submit Branch dropdown AJX===========
def load_branch(request):
    comId = int(request.GET.get('comName'))
    branch = Branch.objects.filter(comId=comId).order_by('branchName')
    return render(request, 'ajx-submit-branch-dropdown.html', {'branch': branch})

# ==========Offer Submit Page===========
def getsubmition(request):
    if request.user.is_authenticated:
        u=get_object_or_404(User, id=request.user.id)
        form = PostForm(request.user, request.POST or None, request.FILES or None)
        formCoupon = CouponForm(request.POST or None)
        formFeature = FeaturedPostForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author=u
            instance.branch== request.POST.get('branch')
            instance.save()
            if formCoupon.is_valid():
                instance2 = formCoupon.save(commit=False)
                instance2.postId=get_object_or_404(Post,id=instance.id)
                instance2.save()
            if formFeature.is_valid():
                instance3 = formFeature.save(commit=False)
                instance3.postId=get_object_or_404(Post,id=instance.id)
                instance3.save()
            return redirect('index')
        return render(request, "submit-coupon.html", {"form": form, "formCoupon": formCoupon,"formFeature":formFeature})
    else:
        return redirect('login')

# ==========Login Page===========
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

# ==========Signup Page===========
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
            newFirstName = first_name.replace(" ", "")
            i = 0
            for u in usr:
                if u.username == newFirstName or u.username == newFirstName + str(i):
                    i = i + 1
                else:
                    pass
            if i==0:
                instance.username = newFirstName
            else:
                instance.username = newFirstName + str(i)
            instance.save()
            return HttpResponse("You are registered. Click <a href='/login'>here</a> to login")
        else:
            return redirect("signup")

# ==========Logout function===========
def getlogout(request):
    logout(request)
    return redirect('index')
