from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class City(models.Model):
    city_name = models.CharField(
        max_length=128, verbose_name=_("Название"), unique=True
    )

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = _("Город")
        verbose_name_plural = _("Города")


class BrandStore(models.Model):
    brand_name = models.CharField(
        max_length=128, verbose_name=_("Название магазина"), unique=True
    )

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = _("Брэнд магазина")
        verbose_name_plural = _("Брэнды Магазинов")


class BrandVacancy(models.Model):
    vacancy_name = models.CharField(
        max_length=128, blank=False, null=False, verbose_name=_("Название вакансии")
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("Город"),
        related_name="vacancies",
    )
    brand = models.ForeignKey(
        BrandStore,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("Брэнд магазина"),
        related_name="vacancies",
    )
    hourly_rate = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name=_("Часовая ставка"),
        blank=True,
        null=True,
    )
    vacancy_count = models.PositiveIntegerField(
        verbose_name=_("Количество вакансий"), default=0
    )

    def __str__(self):
        return self.vacancy_name

    def increase(self, count: int = 1):
        self.vacancy_count += count
        self.save()

    def decrease(self, count: int = 1):
        self.vacancy_count -= count
        self.save()

    class Meta:
        indexes = [
            models.Index(fields=["city"]),
            models.Index(fields=["brand"]),
        ]
        verbose_name = _("Вакансия")
        verbose_name_plural = _("Вакансии")


class ClientPersonInfo(models.Model):
    class CommunicateSelect(models.TextChoices):
        TELEGRAM = "telegram", _("Telegram")
        WHATSAPP = "whatsapp", _("WhatsApp")
        PHONE = "phone", _("Телефон")

    client_name = models.CharField(
        max_length=128, blank=False, null=False, verbose_name=_("ФИО Клиента")
    )
    phone = models.CharField(
        max_length=21, blank=False, null=False, verbose_name=_("Телефон")
    )
    vacancy = models.ForeignKey(
        BrandVacancy,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Выбраная вакансия",
    )
    preferred_communication = models.CharField(
        max_length=10,
        choices=CommunicateSelect,
        blank=False,
        null=False,
        verbose_name=_("Предпочитаемый способ связи"),
        default=CommunicateSelect.PHONE,
    )
    telegram_username = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_("Логин в Telegram"),
        help_text=_("Логин указывается через @"),
    )
    status = models.BooleanField(
        default=False, blank=False, null=False, verbose_name=_("Статус заявки")
    )

    def clean(self):
        super().clean()
        if (
            self.preferred_communication == self.CommunicateSelect.TELEGRAM
            and not self.telegram_username
        ):
            raise ValidationError(
                {
                    "telegram_username": _(
                        "Для выбранного способа связи 'Telegram' необходимо указать имя пользователя."
                    )
                }
            )

        if self.status and self.vacancy.vacancy_count < 1:
            raise ValidationError(
                {
                    "status": _(
                        "Невозможно изменить статус из-за отсутсвия доступных вакансий"
                    )
                }
            )

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = "Персональную информацию"
        verbose_name_plural = "Клиенты"
