# Generated by Django 5.1.5 on 2025-01-29 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0003_remove_brandvacancy_vacancy_name_ky_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Client",
            new_name="ClientPersonInfo",
        ),
    ]
