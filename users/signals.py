from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def build_profile_on_creation(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save(sender, instance, created, **kwargs):
    instance.profile.save()
