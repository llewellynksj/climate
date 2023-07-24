from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})


def people(request):
    return render(request, 'people.html', {})
