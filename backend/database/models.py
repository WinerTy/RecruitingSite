from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import gettext as _
from django.utils import translation


class LangSelector(models.TextChoices):
    @classmethod
    def language_choices(cls):
        return [(lang[0], _(lang[1])) for lang in settings.LANGUAGES]


class City(models.Model):
    city_name = models.CharField(
        max_length=128, verbose_name=_("Название города"), unique=True
    )

    def __str__(self):
        return self.city_name

    @property
    def translated_city_name(self):
        current_language = translation.get_language()
        try:
            translation_obj = self.translations.get(language_code=current_language)
            return translation_obj.translation or self.city_name
        except ObjectDoesNotExist:
            return self.city_name

    class Meta:
        verbose_name = _("Город")
        verbose_name_plural = _("Города")


class CityTranslation(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name=_("Город"),
        related_name="translations",
    )
    translation = models.CharField(
        verbose_name=_("Перевод"),
        max_length=128,
        blank=True,
        null=True,
    )
    language_code = models.CharField(
        verbose_name=_("Языка"),
        max_length=2,
        choices=LangSelector.language_choices(),
    )

    def __str__(self):
        return self.city.city_name

    class Meta:
        unique_together = ("city", "language_code")
        verbose_name = _("Перевод городов")
        verbose_name_plural = _("Переводы городов")


class Site(models.Model):
    site_name = models.CharField(
        max_length=128, verbose_name=_("Название магазина"), unique=True
    )

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = _("Сайт магазина")
        verbose_name_plural = _("Сайты Магазинов")


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
    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("Сайт"),
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

    @property
    def translated_vacancy_name(self):
        current_language = translation.get_language()
        try:
            translation_obj = self.translations.get(language_code=current_language)
            return translation_obj.translation or self.vacancy_name
        except ObjectDoesNotExist:
            return self.vacancy_name

    class Meta:
        indexes = [
            models.Index(fields=["city"]),
            models.Index(fields=["site"]),
        ]
        verbose_name = _("Вакансия")
        verbose_name_plural = _("Вакансии")


class BrandVacancyTranslation(models.Model):
    vacancy = models.ForeignKey(
        BrandVacancy, on_delete=models.CASCADE, related_name="translations"
    )
    translation = models.CharField(verbose_name=_("Перевод"), max_length=128)
    language_code = models.CharField(
        max_length=2, choices=LangSelector.language_choices(), verbose_name=_("Язык")
    )

    def __str__(self):
        return self.vacancy.vacancy_name

    class Meta:
        unique_together = ("vacancy", "language_code")
        verbose_name = _("Перевод")
        verbose_name_plural = _("Перевод")


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
