from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import PostCategory
from .tasks import new_post_add

@receiver(m2m_changed, sender=PostCategory)
def notify_subs(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        new_post_add()