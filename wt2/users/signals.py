from  django.db.models.signals import post_save #signal that fires after an object is saved
from django.contrib.auth.models import User #the sender of the signal
from django.dispatch import receiver #the receiver will be a function
from .models import Profile

"""
    in order to create a profile instance for a newly created user
"""

@receiver(post_save, sender=User)#when a user is saved, send the post_save signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) #create a profile for a created user with that instance


@receiver(post_save, sender=User)#when a user is saved, send the post_save signal
def save_profile(sender, instance, **kwargs):
    instance.profile.save() #save the profile
