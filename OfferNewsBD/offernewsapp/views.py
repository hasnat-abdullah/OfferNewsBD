from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def getauthor(request, name):
    return render(request, "dashboard.html")


def getcategory(request, name):
    return render(request, "category.html")


def getaboutus(request, id):
    return render(request, "about-us.html")


def getcontact(request, id):
    return render(request, "contact.html")


def getsignin(request, name):
    return render(request, "signin.html")


def getsignup(request, name):
    return render(request, "signup.html")


def getsinglecoupon(request, name):
    return render(request, "dashboard.html")


def getsingledeal(request, name):
    return render(request, "dashboard.html")


def getsinglestore(request, name):
    return render(request, "dashboard.html")


def getstore(request, name):
    return render(request, "dashboard.html")


def getsubmition(request, name):
    return render(request, "dashboard.html")
