from django.shortcuts import render


def index_home(request):
    return render(request, 'index_home.html')


def about_shop(request):
    return render(request, 'about_shop.html')


# def reviews(request):
#     return render(request, 'cart.html')


def catalog(request):
    return render(request, 'catalog.html')
