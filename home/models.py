from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} has got in touch!"


class UserUpdate(models.Model):
    email = models.CharField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} would like to make these changes to their account"
