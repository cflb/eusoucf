from django.shortcuts import render, HttpResponse

# Create your views here.

def website(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')