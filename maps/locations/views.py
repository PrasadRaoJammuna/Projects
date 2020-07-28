from django.shortcuts import render

from django.core.serializers import serialize

from django.http import HttpResponse
from .models import City
from django.contrib.gis.geos import Point
from .data import get_data
# Create your views here.


def home(request):
    return render(request,'index.html')

def city_data(request):
    city = serialize('geojson',City.objects.all())
    return HttpResponse(city,content_type='json')

def add_data(request):

    if request.method == 'POST':
        city = request.POST['city']
        
        obj = City.objects.filter(name=city.title()).count()

        if obj>=1:
           context = {
               'message':'Data already exists..!'
           }

           return render(request,'add.html',context)

        else:
            try:
                name,lat,lon,temp,hum,country = get_data(city)
                obj = City(name=name,coords=Point(lon,lat),temperature=temp,humidity=hum,country=country)
                obj.save()

                context ={
                    'message':'City Added..! Please Visit Home'
                    }
                return render(request,'add.html',context)

            except:
                return HttpResponse('Invalid City Found..!')

           


    return render(request,'add.html')