from django.db import models
import string
import random
# Fat models and thin views!!
# Create your models here.

def generateUniqueCode():
    LENGTH = 6

    while True: #Always generates a random, uppercase code.
        code="".join(random.choices(string.ascii_uppercase, k=length))

        if Room.objects.filter(code=code).count() == 0: #If the code is unique.
            break #Stop generating it.

    return code


class Room(models.Model): #Blueprint for each room.
    code = models.CharField(max_length=8, default=0, unique=True) #Sets the constraints for each room code.
    host = models.CharField(max_length=50, unique=True) #Only 1 host.
    guestCanPause = models.BooleanField(null=False, default=False) #Initially, guests can't pause.
    votesToSkip = models.IntegerField(null=False, default=1)
    createdAt = models.DateTimeField(auto_now_add=True) #Automatically adds the date/time created. 
