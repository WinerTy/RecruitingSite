from rest_framework import serializers

from database.models import BrandVacancy


class VacancySerializer(serializers.ModelSerializer):
    vacancy_name = serializers.CharField(source="translated_vacancy_name")

    class Meta:
        model = BrandVacancy
        fields = ["id", "vacancy_name", "hourly_rate"]
