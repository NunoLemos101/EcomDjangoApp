from Ecom.models import Product
from django.db.models.signals import post_save , post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    if instance.image1 != '3i1415926543PI.jpg':
        instance.image1.delete(False)
    else:
        pass
    instance.image2.delete(False)
    instance.image3.delete(False)
