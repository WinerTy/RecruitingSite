from django.conf import settings
import aiohttp

from database.models import ClientPersonInfo


class TelegramBotController:
    def __init__(
        self, url: str = settings.BOT_URL, admin_id: int = settings.ADMIN_TG_ID
    ):
        self.url = url
        self.admin_id = admin_id

    async def send_message(self, obj: ClientPersonInfo):
        url = f"{self.url}/sendMessage"
        payload = {
            "chat_id": self.admin_id,
            "text": self.formating_message_text(obj),
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                return await response.json()

    def formating_message_text(self, instance: ClientPersonInfo) -> str:
        message = (
            f"У вас новая заявка! Ее уникальный номер {instance.id}\n\n"
            f"Данные пользователя:\n"
            f"ФИО: {instance.client_name}\n"
            f"Телефон: {instance.client_phone}\n"
            f""
        )
        return message
