from django_filters import rest_framework as filters

from database.models import BrandVacancy, City


class VacancyFilter(filters.FilterSet):
    brand = filters.CharFilter(field_name="brand__brand_name")
    city = filters.ModelChoiceFilter(field_name="city", queryset=City.objects.all())

    class Meta:
        model = BrandVacancy
        fields = ["brand"]
