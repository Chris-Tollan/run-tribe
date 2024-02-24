from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))


class Runs(models.Model):
    """
    Stores a run entry related to :model: `runs.Runs`.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Runs'

    def __str__(self):
        return f"Run - {self.title}"


class Booking(models.Model):
    """
     Model representing a booking made by a user for a specific run
     Store a booking made by the user related to 
     :model: `runs.Booking` and :model: `runs.Runs`
    """
    run = models.ForeignKey(
        Runs, on_delete=models.CASCADE, related_name='run_booking')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_booking')
    approved = models.BooleanField(default=False)
    phone = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return f'{self.run.title} is booked by {self.user}'
