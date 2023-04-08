from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone




class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False)
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=3, choices=user_type_data, max_length=10)


    USERNAME_FIELD ="email"
    REQUIRED_FIELDS=["password",]





class Profile(models.Model):
    profile_image = models.TextField(default="/media/profile_images/default_profile.png")
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField( null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.user.email



def save_user_profile(sender, instance, created, *rgs, **kwargs):
    if created:
        Profile.objects.create(
        user=instance,
    )

post_save.connect(save_user_profile, sender=CustomUser)


