from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    """
    This model is an extension of the User model that is inbuilt in django.
    It is connected to django User model with a OneToOneField.
    """
    user = models.OneToOneField(User, related_name="user")
    avatar = models.URLField(blank=False, null=False, max_length=100)
    mobile_number = models.CharField(max_length=20, blank=True, null=False, default="")
    short_bio = models.CharField(max_length=255, blank=False, null=False)
    job_status = models.BooleanField(blank=False, null=False, default=False)
    company_name = models.CharField(blank=True, null=False, default="", max_length=50)
    looking_for_job = models.BooleanField(blank=False, null=False, default=True)
    github_profile = models.URLField(blank=True, null=True, default="", max_length=75)
    facebook_profile = models.URLField(blank=True, null=True, default="", max_length=75)
    twitter_profile = models.URLField(blank=True, null=True, default="", max_length=75)
    linkedin_profile = models.URLField(blank=True, null=True, default="", max_length=75)
    codepen_profile = models.URLField(blank=True, null=True, default="", max_length=75)
    discord_profile = models.CharField(blank=False, null=False, default="", max_length=25)
    familiar_technologies = models.CharField(blank=True, null=False, default="", max_length=255)
    interested_technologies = models.CharField(blank=False, null=False, default="", max_length=255)


def create_user_profile(sender, instance, created, **kwargs):
    """
    This is a post save signal of django user inbuilt model triggers this method.
    :param sender: The model which is responsible for the signal
    :param instance: The instance that was just saved
    :param created: The variable to check if the instance was created
    :param kwargs: other Key value arguments
    """
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
