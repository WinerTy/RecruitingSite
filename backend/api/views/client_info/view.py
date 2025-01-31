from rest_framework.generics import CreateAPIView
from database.models import ClientPersonInfo
from .serializer import ClientPersonInfoCreateSerializer


class ClientPersonInfoCreateView(CreateAPIView):
    queryset = ClientPersonInfo.objects.all()
    serializer_class = ClientPersonInfoCreateSerializer
