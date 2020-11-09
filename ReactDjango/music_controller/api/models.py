from django.db import models
# Create your models here.
# A model is a table in Python and converts it to a Database.

#Django Rule: Fat models, thin views,


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