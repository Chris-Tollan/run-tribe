from django.db import models
from django.contrib.auth.models import User


class UserUpdate(models.Model):
    """
    Stores a details submitted by user for
    account updates
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    email = models.CharField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} would like to make these changes to their account"
