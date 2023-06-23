from django.urls import path, include

from CarCollectionApp.cars.views import create_car, car_details, edit_car, delete_car

urlpatterns = [
    path('create/', create_car, name='create-car'),
    path('<int:pk>/', include([
        path('details/', car_details, name='car-details'),
        path('edit/', edit_car, name='edit-car'),
        path('delete/', delete_car, name='delete-car'),
    ])),

]