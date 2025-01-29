from django_filters import rest_framework as filters

from database.models import BrandVacancy, City, Site


class VacancyFilter(filters.FilterSet):
    site_id = filters.ModelChoiceFilter(field_name="site", queryset=Site.objects.all())
    city_id = filters.ModelChoiceFilter(field_name="city", queryset=City.objects.all())

    class Meta:
        model = BrandVacancy
        fields = ["city_id", "site_id"]
