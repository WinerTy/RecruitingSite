from asgiref.sync import sync_to_async
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ClientPersonInfo
from .tasks.telegram.notify_admin import notify_admin_via_telegram


@receiver(post_save, sender=ClientPersonInfo)
def new_client_watcher(sender, instance, created, **kwargs):
    if created:
        notify_admin_via_telegram.delay(instance.pk)


@receiver(post_save, sender=ClientPersonInfo)
async def change_vacancy_count(sender, instance: ClientPersonInfo, created, **kwargs):
    if instance.status and instance.vacancy.vacancy_count > 0:
        await sync_to_async(instance.vacancy.decrease)()
