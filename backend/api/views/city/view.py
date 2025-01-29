from rest_framework.viewsets import ModelViewSet

from .serializer import CitySerializer
from database.models import City
from api.utils.pagination.paginator import LargeResultSetPagination


class CityViewSet(ModelViewSet):
    queryset = City.objects.order_by("city_name")
    serializer_class = CitySerializer
    http_method_names = ["get", "options"]
    allowed_methods = ["get", "options"]
    pagination_class = LargeResultSetPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
