from django.db import models
from django.contrib.auth.models import User
from PIL import Image


#extending the user model
# Create your models here.
#one to one relationship - one user can have one profile and one profile can have one user


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')
    image = models.ImageField(default='default.jpg', upload_to='media/profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"


    def save(self): #overwrite the .save() method
        super().save()

        img = Image.open(self.image.path) #open the image path of the current instance
        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size) #will resize the image
            img.save(self.image.path) #save the var to the img location