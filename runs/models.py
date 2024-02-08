from django.db import models
from django.contrib.auth.models import User

# Create your models here.


STATUS = ((0, 'Draft'), (1, 'Published'))


class Runs(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Runs'

    def __str__(self):
        return f"Run - {self.title}"


class AvailableRuns(models.Model):
    runs = models.ForeignKey(
        Runs, on_delete=models.CASCADE, related_name='available_runs')

    class Meta:
        verbose_name_plural = 'AvailableRuns'        

    def __str__(self):
        return (
            f'{self.runs} is reserved'
        )
