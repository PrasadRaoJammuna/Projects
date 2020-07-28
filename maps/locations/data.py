import requests
import os
#from .models import City




city='Bangalore' 


def get_data(city):

    key = '06d38de3c75a51c8a59502c50884b828'
    url = 'https://api.openweathermap.org/data/2.5/find?q='+city+'&units=metric&appid='+key
    dataset = requests.get(url).json()
    data = dataset['list'][0]

    name = data['name'].strip()
    lat = float(str(data['coord']['lat']).strip())
    lon = float(str(data['coord']['lon']).strip())
    #c =(lat,lon)
    hum = 'Hum:'+str(data['main']['humidity']).strip()
    temp = 'Temp:'+str(data['main']['temp']).strip()+'°C'
   
    country = data['sys']['country']

    return name,lat,lon,temp,hum,country



#print(get_data(city))