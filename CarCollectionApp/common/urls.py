from django.urls import path

from CarCollectionApp.common.views import home_page, catalogue

urlpatterns = [
    path('', home_page, name='home-page'),
    path('catalogue/', catalogue, name='catalogue'),
]