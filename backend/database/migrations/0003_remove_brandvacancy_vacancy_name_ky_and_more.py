# Generated by Django 5.1.5 on 2025-01-29 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0002_brandvacancy_vacancy_name_ky_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="brandvacancy",
            name="vacancy_name_ky",
        ),
        migrations.RemoveField(
            model_name="brandvacancy",
            name="vacancy_name_ru",
        ),
        migrations.RemoveField(
            model_name="brandvacancy",
            name="vacancy_name_tg",
        ),
        migrations.RemoveField(
            model_name="brandvacancy",
            name="vacancy_name_uz",
        ),
        migrations.CreateModel(
            name="Client",
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
                    "client_name",
                    models.CharField(max_length=128, verbose_name="Имя клиета"),
                ),
                ("phone", models.CharField(max_length=21, verbose_name="Телефон")),
                (
                    "vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database.brandvacancy",
                        verbose_name="Выбраная вакансия",
                    ),
                ),
            ],
        ),
    ]
