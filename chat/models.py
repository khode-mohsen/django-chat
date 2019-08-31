from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Room(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    subscribers = models.ManyToManyField(User, blank=False)
    allow_anonymous_access = models.NullBooleanField()
    private = models.NullBooleanField()
    password = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chat_slug', args=(self.slug))


class Message(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # username field is useful to store guest name of unauthenticated users :)
    username = models.CharField(max_length=20, blank=True)
    date = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=5000)

    def __str__(self):
        return '%s  %s'%(self.user.username, self.room.name)
