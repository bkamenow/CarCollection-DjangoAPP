from CarCollectionApp.cars.models import CarsModel
from CarCollectionApp.profiles.models import ProfileModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return ex


def get_cars():
    return CarsModel.objects.all()


def get_car(pk):
    car = CarsModel.objects.filter(pk=pk).get()
    return car
