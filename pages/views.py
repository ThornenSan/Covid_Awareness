from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def symtoms_analysis(request):
    return render(request, 'pages/symtoms analysis.html')


def hospitals_details(request):
    return render(request, 'pages/hospital details.html')


def contact(request):
    return render(request, 'pages/contact.html')
