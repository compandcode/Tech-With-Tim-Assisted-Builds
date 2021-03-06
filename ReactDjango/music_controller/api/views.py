from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
class RoomView(generics.CreateAPIView): #Blueprint for viewing rooms and creating them. ***** Create/List.
    querySet = Room.objects.all() #Stores all the rooms.
    serializer_class = RoomSerializer #Converts the rooms into a more comprehendable format.

