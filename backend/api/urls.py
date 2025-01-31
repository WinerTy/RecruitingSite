from django.urls import path, include
from .views.router import router as api_router
from .views.client_info.view import ClientPersonInfoCreateView

urlpatterns = [
    path(
        "client/person-info/create/",
        ClientPersonInfoCreateView.as_view(),
        name="client-person-info-create",
    ),
]


urlpatterns += [path("", include(api_router.urls))]
