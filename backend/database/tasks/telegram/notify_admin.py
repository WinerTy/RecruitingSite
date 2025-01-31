import requests
from celery import shared_task
from django.conf import settings

from database.models import ClientPersonInfo
from database.tasks.utils.formated_message import formating_message_text


@shared_task
def notify_admin_via_telegram(obj_id: int) -> None:
    try:
        obj: ClientPersonInfo = ClientPersonInfo.objects.get(id=obj_id)
        message: str = formating_message_text(obj)
        url: str = f"{settings.BOT_URL}/sendMessage"
        payload = {
            "chat_id": settings.ADMIN_TG_ID,
            "text": message,
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(e)
