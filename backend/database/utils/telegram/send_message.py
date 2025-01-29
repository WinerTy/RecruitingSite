from django.conf import settings
import aiohttp


async def get_admin_id() -> int:
    return settings.ADMIN_TG_ID


async def send_message(message: str):
    url = f"{settings.BOT_URL}/sendMessage"
    payload = {
        "chat_id": await get_admin_id(),
        "text": message,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            return await response.json()
