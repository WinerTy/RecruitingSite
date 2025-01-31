from database.models import ClientPersonInfo


def formating_message_text(obj: ClientPersonInfo) -> str:
    message = (
        f"У вас новая заявка! Ее уникальный номер {obj.id}\n\n"
        f"Данные пользователя:\n"
        f"ФИО: {obj.client_name}\n"
        f"Телефон: {obj.client_phone}\n"
        f"Способ связи: {obj.get_preferred_communication_display()}\n"
        f"Логин Telegram: {obj.telegram_username}\n\n"
        f"Сайт: {obj.vacancy.site.site_name}"
    )
    return message
