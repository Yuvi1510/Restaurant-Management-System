from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UserProfile
from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def user_created_or_updatted(sender,instance,created,**kwargs):
#     if created:
#         UserProfile.objects.create(instance=User)
#     instance.UserProfile.save()