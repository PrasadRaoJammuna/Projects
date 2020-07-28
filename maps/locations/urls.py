from django.urls import path

from .views import home,city_data,add_data

urlpatterns = [
    path('',home,name='home'), 
    path('citydata/',city_data,name='citydata'),
    path('data/',add_data,name='data'),
]