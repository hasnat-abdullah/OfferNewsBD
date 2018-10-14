from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def getauthor(request, name):
    return render(request, "dashboard.html")


def getcategory(request):
    return render(request, "category.html")


def getaboutus(request):
    return render(request, "about-us.html")


def getcontact(request):
    return render(request, "contact.html")


def getsignin(request):
    return render(request, "signin.html")


def getsignup(request):
    return render(request, "signup.html")


def getsinglecoupon(request, name):
    return render(request, "single-coupon-code.html")


def getsingledeal(request, name):
    return render(request, "single-coupon-sale.html")


def getsinglestore(request, name):
    return render(request, "single-store.html")


def getstore(request):
    return render(request, "stores.html")


def getsubmition(request):
    return render(request, "submit-coupon.html")
