from django.shortcuts import render, redirect
from .models import  PredictResult, MapLocation
from .filter_model import predict_model
import folium
from folium.plugins import FastMarkerCluster 
# Create your views here.
def index(request):
    items = PredictResult.objects.all()

    context = {
        'items': items,
    }
    return render(request, 'base/index.html', context)
def add_photo(request):

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        phone = PredictResult.objects.create(
            name = data['name'],
            image = image,
        )
        pred = predict_model(image)
        
        
        defaults = {'result':pred}
        try:
            obj = PredictResult.objects.get(name=data['name'], image=image)
            for key, value in defaults.items():
               setattr(obj, key, value)
            obj.save()
        except PredictResult.DoesNotExist:
            new_val = {'name':data['name'], 'image':image}
            obj = PredictResult(**new_val)
            obj.save()  
        return redirect('index')
    
    return render(request, 'base/add.html')

def add_map(request):
    df = MapLocation.objects.all()
    m = folium.Map(location = [37.5519, 126.9918], zoom_stop=9)
    latitudes = [x.latitude for x in df]
    longitudes = [x.longitude for x in df]
    for d in df:
        coordinates = (d.latitude, d.longitude)
        folium.Marker(coordinates, popup=d.date).add_to(m)
    m2 = folium.Map(location =[41.5025, -102.699997], zoom_stop=2)
    
    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m2)
    context = {
        "map": m._repr_html_(),
        "map2":m2._repr_html_()
    }
    return render(request, 'base/map.html', context)