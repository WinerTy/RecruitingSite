from rest_framework.viewsets import ModelViewSet

from .serializer import CitySerializer
from database.models import City


class CityViewSet(ModelViewSet):
    queryset = City.objects.order_by("name")
    serializer_class = CitySerializer
    http_method_names = ["get", "options"]
    allowed_methods = ["get", "options"]
