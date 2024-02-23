from django.db import models


class ContactUs(models.Model):
    """
    Stores a contact us message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} has got in touch!"
