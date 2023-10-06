from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def assign_user_to_client_group(sender, instance, created, **kwargs):
    if created:
        client_group, created = Group.objects.get_or_create(name='Client')
        instance.groups.add(client_group)
