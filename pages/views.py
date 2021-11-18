from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    context = {}
    request.session.set_expiry(request.session.get_expiry_age())
    return render(request, "pages/Homepage.html", context)

def reviews_view(request, *args, **kwargs):
    context = {}
    request.session.set_expiry(request.session.get_expiry_age())
    return render(request, "pages/book-reviews.html", context)

def recommendations_view(request, *args, **kwargs):
    #request.session.set_expiry(request.session.get_expiry_age())
    return HttpResponse("<h1>Page under construction</h1>") # no html

def lists_view(request, *args, **kwargs):
    context = {}
    #request.session.set_expiry(request.session.get_expiry_age())
    return render(request, "pages/Lists.html", context)

def login_view(request, *args, **kwargs):
    context = {}
    #request.session.set_expiry(request.session.get_expiry_age())
    return render(request, "pages/Myprofile-before.html", context)

def topbooks_view (request, *args, **kwargs):
    context = {}
    #request.session.set_expiry(request.session.get_expiry_age())
    return render(request, "pages/Top-books.html", context)

def foryou_view (request, *args, **kwargs):
    context = {}
    #request.session.set_expiry(request.session.get_expiry_age())
    return render(request, "pages/For-you.html", context)

def topauthors_view(request, *args, **kwargs):
    #request.session.set_expiry(request.session.get_expiry_age())
    return HttpResponse("<h1>Page under construction</h1>") # no html

def topgenres_view(request, *args, **kwargs):
    #request.session.set_expiry(request.session.get_expiry_age())
    return HttpResponse("<h1>Page under construction</h1>") # no html

def mybooks_view(request, *args, **kwargs):
    #request.session.set_expiry(request.session.get_expiry_age())
    return HttpResponse("<h1>Page under construction</h1>") # no html