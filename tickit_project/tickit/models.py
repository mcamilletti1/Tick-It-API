from django.db import models

# Create your models here.


class Venue(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    photo_url = models.TextField(
        default="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png")

    def __str__(self):
        return self.name


class Event(models.Model):
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default="Event")
    photo_url = models.TextField(
        default="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png")
    
    def venue_name(self):
        return self.venue.name

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField()
    event_id = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name
