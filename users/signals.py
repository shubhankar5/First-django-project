from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Address


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)
		Address.objects.create(profile=instance.profile)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()
	instance.profile.address.save()

