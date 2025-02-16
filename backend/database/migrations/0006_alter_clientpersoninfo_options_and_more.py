# Generated by Django 5.1.5 on 2025-01-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0005_clientpersoninfo_preferred_communication_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="clientpersoninfo",
            options={
                "verbose_name": "Персональная информация",
                "verbose_name_plural": "Персональная Информация",
            },
        ),
        migrations.AlterField(
            model_name="clientpersoninfo",
            name="client_name",
            field=models.CharField(max_length=128, verbose_name="ФИО Клиента"),
        ),
        migrations.AlterField(
            model_name="clientpersoninfo",
            name="telegram_username",
            field=models.CharField(
                blank=True,
                help_text="Логин указывается через @",
                max_length=128,
                null=True,
                verbose_name="Логин в Telegram",
            ),
        ),
    ]
