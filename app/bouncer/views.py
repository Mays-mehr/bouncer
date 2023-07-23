from django.shortcuts import render


def landing(request):
    """render the index page"""
    return render(request , 'bouncer/index.html')


