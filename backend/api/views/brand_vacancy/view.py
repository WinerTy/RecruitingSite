from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.utils.pagination.paginator import LargeResultSetPagination
from api.views.brand_vacancy.filter import VacancyFilter
from api.views.brand_vacancy.serializer import VacancySerializer
from database.models import BrandVacancy


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = BrandVacancy.objects.filter(vacancy_count__gt=0).order_by("vacancy_name")
    serializer_class = VacancySerializer
    pagination_class = LargeResultSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VacancyFilter
