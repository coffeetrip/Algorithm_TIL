from django.shortcuts import render

# Create your views here.
def map(request):
    return render(request, 'map.html')


def geocoder(request):
    return render(request, 'geocoder.html')