from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here. (Endpoints).
# Note: Both Functions and Classes can be used as views.

#API View to view a list of all the different views.
class RoomView(generics.ListAPIView): #Room to setup and return all the different Rooms. Change 'List' to 'Create' if you want to input. 
    queryset = Room.objects.all() #Gets all the Room Objects.
    serializer_class = RoomSerializer #Converts it to a better format.