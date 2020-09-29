from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Animal(models.Model):
    """Model representing animal in a shelter."""
    name = models.CharField(max_length=200, help_text="Enter a animal name.")
    age = models.IntegerField(help_text="Enter a animal age (integer).")
    date_of_arrival = models.DateField(help_text="Enter a date of arrival (yyyy-mm-dd).")
    weight = models.FloatField(help_text="Enter a animal weight.")
    height = models.FloatField(help_text="Enter a animal height.")
    special_signs = models.CharField(
        max_length=200,
        help_text="Enter a animal special signs"
    )
    shelter = models.ForeignKey('Shelter', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular shelter instance.
        """
        return reverse('animal-detail', args=[str(self.id)])

    def __str__(self) -> str:
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Shelter(models.Model):
    """Model representing shelter."""
    name = models.CharField(max_length=200, help_text="Enter a shelter name")

    def get_absolute_url(self):
        """
        Returns the url to access a particular shelter instance.
        """
        return reverse('shelter-detail', args=[str(self.id)])

    def __str__(self) -> str:
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shelter = models.ForeignKey('Shelter', on_delete=models.SET_NULL, null=True)
    role = models.IntegerField(default=0)

    @property
    def is_admin(self) -> bool:
        return self.role == 2

    @property
    def is_user(self) -> bool:
        return self.role == 1

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Client.objects.create(user=instance)
        instance.client.save()

    def __str__(self) -> str:
        """String for representing the Model object (in Admin site etc.)"""
        return self.user.username
