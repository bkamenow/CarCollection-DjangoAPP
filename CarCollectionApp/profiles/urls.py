from django.urls import path, include

from CarCollectionApp.profiles.views import profile_details, edit_profile, delete_profile, create_profile

urlpatterns = [
    path('create/', create_profile, name='create-profile'),
    path('details/', profile_details, name='profile-details'),
    path('edit/', edit_profile, name='edit-profile'),
    path('delete/', delete_profile, name='delete-profile'),
]