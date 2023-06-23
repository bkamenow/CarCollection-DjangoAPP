from django.shortcuts import render, redirect

from CarCollectionApp.cars.forms import CreateCarForm, EditCarForm, DeleteCarForm
from helpers.helper import get_profile, get_car


# Create your views here.


def create_car(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template_name='cars/car-create.html', context=context)


def car_details(request, pk):
    profile = get_profile()
    car = get_car(pk)

    context = {
        'profile': profile,
        'car': car,
    }
    return render(request, template_name='cars/car-details.html', context=context)


def edit_car(request, pk):
    profile = get_profile()
    car = get_car(pk)

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form,
        'car': car,
    }

    return render(request, template_name='cars/car-edit.html', context=context)


def delete_car(request, pk):
    profile = get_profile()
    car = get_car(pk)

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'profile': profile,
        'car': car,
        'form': form,
    }

    return render(request, template_name='cars/car-delete.html', context=context)
