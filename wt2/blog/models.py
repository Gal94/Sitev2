from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #set date time only when post is created
    author = models.ForeignKey(User, on_delete='CASCADE') #FOREIGN KEY = ONE TO MANY, 1 author many posts

    def __str__(self):
        return self.title

    def get_absolute_url(self): #creates a path to a specific post to be directed to
        return reverse('blog:post-detail',kwargs={'pk':self.pk}) #return post-detail and the primary key of the post as variable pk.
