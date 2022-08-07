
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    context= {
        "title": "Home Page"
        "content": "Welcome to the home page"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context= {
        "title": "About"
        "content": "Welcome to About page"
    }
    return render(request, "about_page.html", context)

    def contact_page(request):
    context= {
        "title": "Contact"
        "content": "Welcome to the Contact page"
    }
    return render(request, "contact_page.html", context)