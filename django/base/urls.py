from django.urls import path
from .views import index, add_photo, add_map
urlpatterns = [
    path('', index, name='index'),
    path('add_photo/', add_photo, name='add_photo'),
    path('add_map/', add_map, name='add_map')
]