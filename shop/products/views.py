from django.shortcuts import render


def index(request):
    context = {
        'title': 'Привет'
    }
    return render(request, 'products/index.html', context)
