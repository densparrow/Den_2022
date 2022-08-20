from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about_us.html')


def my_page(request):
    return render(request, 'main/my_page.html')
