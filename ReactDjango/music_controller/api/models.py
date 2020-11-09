from django.db import models #Allows us to create a Django DB.
import string #Allows us to access ASCII.
import random #Allows us to randomly generate codes.

def generate_unique_code():
    length = 6 #Arbritary.
    
    while True: #Always.
        """
            Generates a random code of K length.
            Only contains the UPPERCASE Ascii characters.
            Joins it to a string that's initially blank,
        """
        code="".join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code) == 0: #If they're different.
            break #Stop generating.
    return code#Return the code to the function.


# Create your models here.
# A model is a table in Python and converts it to a Database.

#Django Rule: Fat models, thin views. Majority of logic should go on models.


class Room(models.Model):  # The Room is going to be a model.
    #Class attributes for each room:
    # Unique code for each room (characters). Constraints shown.
    code = models.CharField(max_length=8, default="", unique=True)
    # Stores information relating to the host of the room. Keeps track of them.
    host = models.CharField(max_length=50, unique=True)
    # States by default they shouldn't be able to pause.
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    # Date/Time is automatically added, we don't need to pass it.
    created_at = models.DateTimeField(auto_now_add=True)