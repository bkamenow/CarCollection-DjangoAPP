from django.shortcuts import render

from helpers.helper import get_profile, get_cars


# Create your views here.


def home_page(request):
    profile = get_profile()
    cars = get_cars()

    context = {
        'profile': profile,
        'cars': cars,
    }
    return render(request, template_name='common/index.html', context=context)


def catalogue(request):
    profile = get_profile()
    cars = get_cars()

    context = {
        'profile': profile,
        'cars': cars
    }
    return render(request, template_name='common/catalogue.html', context=context)
