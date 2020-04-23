from django.shortcuts import render, HttpResponse


def website(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')