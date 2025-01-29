from asgiref.sync import sync_to_async
from django.db import IntegrityError
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from .models import ClientPersonInfo
from .utils.telegram.send_message import TelegramBotController


@receiver(post_save, sender=ClientPersonInfo)
async def notify_admin_via_telegram(
    sender, instance: ClientPersonInfo, created, **kwargs
):
    if created:
        controller = TelegramBotController()
        await controller.send_message(obj=instance)


@receiver(post_save, sender=ClientPersonInfo)
async def change_vacancy_count(sender, instance: ClientPersonInfo, created, **kwargs):
    if instance.status and instance.vacancy.vacancy_count > 0:
        await sync_to_async(instance.vacancy.decrease)()
