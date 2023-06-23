from django.shortcuts import render, redirect

from CarCollectionApp.cars.forms import DeleteCarForm
from CarCollectionApp.profiles.forms import CreateProfileForm, DeleteProfileForm, EditProfileForm
from helpers.helper import get_profile, get_cars


# Create your views here.


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form
    }

    return render(request, template_name='profile/profile-create.html', context=context)


def profile_details(request):
    profile = get_profile()
    cars = get_cars()

    total_price = sum([s.price for s in cars])

    context = {
        'profile': profile,
        'total_price': total_price,
    }
    return render(request, template_name='profile/profile-details.html', context=context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template_name='profile/profile-edit.html', context=context)


def delete_profile(request):
    profile = get_profile()
    cars = get_cars()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()
        for car in cars:
            car_form = DeleteCarForm(request.POST, instance=car)
            car_form.save()

        return redirect('home-page')

    context = {
        'profile': profile
    }

    return render(request, template_name='profile/profile-delete.html', context=context)
