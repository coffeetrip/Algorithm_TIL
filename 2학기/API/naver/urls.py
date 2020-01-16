from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map),
    path('geocoder/', views.geocoder),

]
