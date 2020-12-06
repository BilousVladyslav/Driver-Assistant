from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from . import managers


class Coordinates(models.Model):
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)


class Car(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=150, blank=False)
    number = models.CharField(max_length=10, blank=True)
    is_special = models.BooleanField(default=False, blank=False)
    coordinates = models.OneToOneField(Coordinates, on_delete=models.CASCADE, blank=True, null=True)


@receiver(post_save, sender=Car)
def create_coordinates(sender, instance=None, created=False, **kwargs):
    if created:
        coords = Coordinates.objects.create(latitude=50.005942, longitude=36.229618)
        instance.coordinates = coords
        instance.save()
