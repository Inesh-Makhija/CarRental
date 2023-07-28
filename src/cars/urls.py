
from django.urls import path

from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.car_list_view, name = 'list'),
    path('create/', views.car_create_view, name='create'),
]
