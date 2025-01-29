# Generated by Django 5.1.5 on 2025-01-28 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BrandStore",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "brand_name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="Название магазина"
                    ),
                ),
            ],
            options={
                "verbose_name": "Брэнд магазина",
                "verbose_name_plural": "Брэнды Магазинов",
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "city_name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
            },
        ),
        migrations.CreateModel(
            name="BrandVacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vacancy_name",
                    models.CharField(max_length=128, verbose_name="Название вакансии"),
                ),
                (
                    "hourly_rate",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=8,
                        null=True,
                        verbose_name="Часовая ставка",
                    ),
                ),
                (
                    "vacancy_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество вакансий"
                    ),
                ),
                (
                    "brand_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database.brandstore",
                        verbose_name="Брэнд магазина",
                    ),
                ),
                (
                    "city_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database.city",
                        verbose_name="Город",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вакансия",
                "verbose_name_plural": "Вакансии",
            },
        ),
    ]
