from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import File



@receiver(post_delete, sender=File)
def delete_related_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(save=False)
