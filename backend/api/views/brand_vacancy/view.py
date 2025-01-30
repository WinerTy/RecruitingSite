from rest_framework.exceptions import ValidationError, MethodNotAllowed
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from api.utils.pagination.paginator import LargeResultSetPagination
from api.views.brand_vacancy.filter import VacancyFilter
from api.views.brand_vacancy.serializer import VacancySerializer
from database.models import BrandVacancy


class VacancyViewSet(ModelViewSet):
    queryset = BrandVacancy.objects.filter(vacancy_count__gt=0).order_by("vacancy_name")
    serializer_class = VacancySerializer
    pagination_class = LargeResultSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VacancyFilter
    http_method_names = ["get", "options"]
    allowed_methods = ("get", "options")

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return BrandVacancy.objects.none()

        city_id = self.request.query_params.get("city_id", None)
        site_id = self.request.query_params.get("site_id", None)

        if city_id is None or site_id is None:
            raise ValidationError(
                {"detail": ["Параметры city_id и site_id обязательные"]}
            )

        return super().get_queryset()

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET", detail="Детальный просмотр записи недоступен.")
