from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def login(request):
    return render(request, 'pages/login.html')


def symtoms_analysis(request):
    return render(request, 'pages/symtoms analysis.html')


def hospitals_details(request):
    return render(request, 'pages/hospital details.html')


def contact(request):
    return render(request, 'pages/contact.html')


def register(request):
    return render(request, 'pages/register.html')
