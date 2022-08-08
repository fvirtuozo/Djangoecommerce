
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context= {
        'title': 'Home Page',
        'content': 'Welcome to the home page'
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context= {
        'title': 'About',
        'content': 'Welcome to About page'
    }
    return render(request, "about/view.html", context)
   
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
    
        "title": "Página de contato",
        "content": "Bem-vindo a página de contato",
        "form": contact_form
    }
   
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('Nome_Completo'))
        print(request.POST.get('email'))
        print(request.POST.get('Mensagem'))
    return render(request, "contact/view.html", context)